import streamlit as st
import pandas as pd

# Configure the page
st.set_page_config(page_title="Relu Data Extractor", page_icon="📊", layout="wide")

st.sidebar.title("Navigation")
st.sidebar.markdown("Relu Consultancy Hiring Challenge")
challenge = st.sidebar.radio("Select Target:", ["Disney Cruise", "Ingredients Network"])

if challenge == "Disney Cruise":
    st.title("🚢 Disney Cruise Data Extractor")
    st.markdown("Extracted cruise itineraries, destinations, and pricing metadata.")
    
    try:
        df = pd.read_csv("Disney_Cruise_Results.csv")
        st.success(f"Successfully loaded {len(df)} records.")
        
        # Display the required analytical answers
        st.subheader("Hackathon Analytics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Cruises", "111")
        col2.metric("Pacific Destinations", "2")
        col3.metric("Holiday Cruises", "48")
        
        col4, col5, col6 = st.columns(3)
        col4.metric("Cruises > 2 Booking Dates", "48")
        col5.metric("Miami/London Departures", "0")
        
        st.subheader("Extracted Dataset")
        st.dataframe(df, use_container_width=True)
        
    except FileNotFoundError:
        st.warning("Disney_Cruise_Results.csv not found. Please ensure the file is in the root directory.")

elif challenge == "Ingredients Network":
    st.title("🌿 Ingredients Network Extractor")
    st.markdown("Extracted company profiles, contact details, and category metadata.")
    
    try:
        df = pd.read_csv("Ingredients_Network_Final.csv")
        st.success(f"Successfully loaded {len(df)} records.")
        
        # Display the required analytical answers
        st.subheader("Hackathon Analytics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingredients", "522")
        col2.metric("Finished Products", "207")
        col3.metric("Herbs & Spices", "26")
        
        col4, col5, col6 = st.columns(3)
        col4.metric("Physical Delivery Formats", "32")
        col5.metric("Cognitive & Mental Health", "21")
        
        st.subheader("Extracted Dataset")
        st.dataframe(df, use_container_width=True)
        
    except FileNotFoundError:
        st.warning("Ingredients_Network_Final.csv not found. Please ensure the file is in the root directory.")