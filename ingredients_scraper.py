from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import re

SEARCH_URL = "https://www.ingredientsnetwork.com/live/search/searchresults46v2.jsp?site=47&SugType_val=&RecordId_val=&searchtype=all&name="

def scrape_ingredients_network():
    all_companies = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("STAGE 1: Fetching Search Page & Expanding All Results...")
        page.goto(SEARCH_URL, timeout=60000)
        page.wait_for_selector('.result_company', timeout=15000)
        
        # --- PAGINATION LOOP ---
        click_count = 0
        while True:
            try:
                load_more_btn = page.locator('a.button-secondary:has-text("Show more results")')
                
                if load_more_btn.is_visible(timeout=3000):
                    load_more_btn.scroll_into_view_if_needed()
                    load_more_btn.click(force=True)
                    click_count += 1
                    print(f"Clicked 'Show more results' (Page {click_count + 1}). Waiting for cards to load...")
                    page.wait_for_timeout(2500) 
                else:
                    print("No more results button visible. Reached the end of the directory!")
                    break
            except Exception:
                print("Finished expanding pages.")
                break
        
        soup = BeautifulSoup(page.content(), 'html.parser')
        cards = soup.find_all(class_='result_company')
        print(f"\n✅ Total companies found after expanding: {len(cards)}. Preparing for deep extraction...\n")
        
        for index, card in enumerate(cards):
            h3 = card.find('h3')
            img = card.find('img')
            paragraphs = card.find_all('p')
            
            if not (h3 and img and img.get('src')):
                continue
                
            company_name = h3.text.strip()
            
            description = ""
            for p_tag in paragraphs:
                text = p_tag.text.strip()
                if text and text != "Company":
                    description = text
                    break
            
            src = img['src']
            comp_id_match = re.search(r'(comp\d+)', src)
            if not comp_id_match:
                continue
                
            comp_id = comp_id_match.group(1)
            slug = re.sub(r'[^a-z0-9]+', '-', company_name.lower()).strip('-')
            profile_url = f"https://www.ingredientsnetwork.com/{slug}-{comp_id}.html"
            
            print(f"[{index + 1}/{len(cards)}] Scraping: {company_name}")
            
            # STAGE 2: Deep Profile Extraction
            try:
                page.goto(profile_url, timeout=45000)
                page.wait_for_timeout(2000)
                
                profile_soup = BeautifulSoup(page.content(), 'html.parser')
                text_lines = [line.strip() for line in profile_soup.get_text(separator='\n').split('\n') if line.strip()]
                
                data = {
                    "Company Name": company_name,
                    "Description": description,
                    "Sales Markets": "N/A",
                    "Primary Business Activity": "N/A",
                    "Categories": "N/A",
                    "Events": "N/A",
                    "Address": "N/A",
                    "Email": "N/A",
                    "Telephone": "N/A",
                    "Website": "N/A",
                    "Profile URL": profile_url
                }
                
                labels_to_ignore = ["Email", "Telephone", "Website", "Address", "Contact information", "View all contact information", "Sales markets", "Primary business activity"]
                
                for i, line in enumerate(text_lines):
                    if i + 1 >= len(text_lines):
                        break
                    next_line = text_lines[i+1].strip()
                    
                    if line == "Email" and "@" in next_line:
                        data["Email"] = next_line
                    elif line == "Telephone" and next_line not in labels_to_ignore and len(next_line) > 5:
                        data["Telephone"] = next_line
                    elif line == "Address" and next_line not in labels_to_ignore:
                        data["Address"] = next_line
                    elif line == "Website" and next_line.startswith("http"):
                        data["Website"] = next_line
                    elif line == "Sales markets" and next_line not in labels_to_ignore:
                        data["Sales Markets"] = next_line
                    elif line == "Primary business activity" and next_line not in labels_to_ignore:
                        data["Primary Business Activity"] = next_line
                
                all_companies.append(data)
                
            except Exception as e:
                print(f"  -> Error loading profile: {e}")
                
        browser.close()
        
    return all_companies

def save_data(raw_data):
    if not raw_data:
        print("No data extracted!")
        return
        
    df = pd.DataFrame(raw_data)
    csv_name = "Ingredients_Network_Final.csv"
    df.to_csv(csv_name, index=False)
    print(f"\n✅ SUCCESS: Saved {len(df)} profiles to {csv_name} containing all 10 mandatory fields.")

if __name__ == "__main__":
    extracted_data = scrape_ingredients_network()
    save_data(extracted_data)