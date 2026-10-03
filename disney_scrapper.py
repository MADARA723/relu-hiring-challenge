import requests
import pandas as pd
import time
import json

# Your extracted headers and cookies
import requests

COOKIES = {
    'geolocation_aka_jar': '%7B%22zipCode%22%3A%22%22%2C%22region%22%3A%22MH%22%2C%22country%22%3A%22IN%22%2C%22metro%22%3A%22CHINCHVAD%22%2C%22metroCode%22%3A%22%22%7D',
    'bm_so': 'C69D5A8ED547496333990D5057735A2BAD55C22BA64BFBCC6391C6E8385E5AC3~YAAQZ/naFzFqKvKgAQAA8cGuAAnUU6zBP5IrMC5FpK8cUoI2YRiQKf2EcxWt4a8GIfRUK/PnglIupNmx7jqVyKtAaPsPzToMUZk+BiWE+VqdKi/cjPwWTsGdeeX/9M7iq4Ho291oSXwyGKccLM77E/tX98z9XxJEpAB2Xh/7kaGYUlXpwzWMsaBmIfZxOi4pggA9Y0AlptLowLMG7vJcpaFYd1Txa4vLFRAdakdf5BUC7ann+WOmSyfJdIQGHAaCA9CVDthnKWEayz+2Qt53nT7edDZIUOj/0XJRx1B/SYeDrTPYWGjnk+l9PHCuc6JTIDQj06Ic+yWCB4YBEdrzepIXBzRAK+mRoBnuIDhPNCW7R47YI2zQt/E4GVgKNnOhtK7N0cn8SmXcu4wcbZpDSdaDlUrRJxFJh0lKoarGdLwFHL66stjK2eFIWkrC6/gE8ZsCFZirmKvNB9RDx2WCKEQcsW8zsaqi~4',
    'siteId': 'dcl',
    'localeCookie_jar_aka': '%7B%22contentLocale%22%3A%22en_IN%22%2C%22version%22%3A%222%22%2C%22precedence%22%3A0%2C%22akamai%22%3A%22true%22%2C%22localeCurrency%22%3A%22INR%22%2C%22preferredRegion%22%3A%22en-in%22%7D',
    'languageSelection_jar_aka': '%7B%22preferredLanguage%22%3A%22en_IN%22%2C%22version%22%3A%223%22%2C%22precedence%22%3A0%2C%22language%22%3A%22en_IN%22%2C%22akamai%22%3A%22true%22%7D',
    '_cs_mk_aa': '0.06718367270832759_1791012816035',
    'bm_lso': 'C69D5A8ED547496333990D5057735A2BAD55C22BA64BFBCC6391C6E8385E5AC3~YAAQZ/naFzFqKvKgAQAA8cGuAAnUU6zBP5IrMC5FpK8cUoI2YRiQKf2EcxWt4a8GIfRUK/PnglIupNmx7jqVyKtAaPsPzToMUZk+BiWE+VqdKi/cjPwWTsGdeeX/9M7iq4Ho291oSXwyGKccLM77E/tX98z9XxJEpAB2Xh/7kaGYUlXpwzWMsaBmIfZxOi4pggA9Y0AlptLowLMG7vJcpaFYd1Txa4vLFRAdakdf5BUC7ann+WOmSyfJdIQGHAaCA9CVDthnKWEayz+2Qt53nT7edDZIUOj/0XJRx1B/SYeDrTPYWGjnk+l9PHCuc6JTIDQj06Ic+yWCB4YBEdrzepIXBzRAK+mRoBnuIDhPNCW7R47YI2zQt/E4GVgKNnOhtK7N0cn8SmXcu4wcbZpDSdaDlUrRJxFJh0lKoarGdLwFHL66stjK2eFIWkrC6/gE8ZsCFZirmKvNB9RDx2WCKEQcsW8zsaqi~4~1791012816579',
    'PHPSESSID': 'h9e5iiiap3u1hdjtj0cbkbls13',
    'SWID': '9bf9849f-914e-4411-bbfb-c1a0aad35e2c',
    '__pa': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3OTEwMTI4MTgsImFjY2Vzc190b2tlbiI6ImE2YmI2NzRmM2FjNTRmNTRiYWY1YTk3MWZhNWQ4NDkyIiwidG9rZW5fdHlwZSI6IkJFQVJFUiIsImV4cGlyZXNfaW4iOiIyODgwMCJ9.RQFuHV33Wx89Mn90PuwN5gGDTBBn1lGiRAro4TrhxSjkkvPVBL0Zi3TtjwttOnqoyd-Gw2BtXajb9C_HWXF7VQ',
    'paPublicTokenExpireTime': '1791041558011',
    'at_check': 'true',
    'AMCVS_EDA101AC512D2B230A490D4C%40AdobeOrg': '1',
    's_ecid': 'MCMID%7C57767953894060163791269542447300747941',
    'AMCV_EDA101AC512D2B230A490D4C%40AdobeOrg': '-219703956%7CMCIDTS%7C20730%7CMCMID%7C57767953894060163791269542447300747941%7CMCAAMLH-1791617618%7C12%7CMCAAMB-1791617618%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1791020018s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0',
    'mboxEdgeCluster': '41',
    'kndctr_EDA101AC512D2B230A490D4C_AdobeOrg_identity': 'CiY1Nzc2Nzk1Mzg5NDA2MDE2Mzc5MTI2OTU0MjQ0NzMwMDc0Nzk0MVIRCK2hu4WQNBgBKgRJTkQxMAPwAa2hu4WQNA==',
    'kndctr_EDA101AC512D2B230A490D4C_AdobeOrg_cluster': 'ind1',
    '_fbp': 'fb.1.1791012818979.98616861979130515',
    '_gcl_au': '1.1.1246652143.1791012821',
    'ak_bmsc': '549D2C7DF47D0EA564257DF032166452~000000000000000000000000000000~YAAQZ/naFxaSKvKgAQAAjT6xAAGp7dMz2EyVE1Jt6wJKD8niCJTrW2bhUH042deq32E4p/oNJpxTGuV/a5BjTP4kJIJq9x1z62RUSziViGPtOErDIaOZV5BDJULsmrL+Q67jlFWvnOyUf08MHxrZWKxuVWtF9v65i2iT6FxP7cAuBA1nUIx/sRTGgdOsHBjhis5eoX3mxOcUeVuOHWWl4k7SXAFHl/o/vMMDr8+mQvPlPxNOUX65CwpwMKwIFIcGDX4hCnI1mQlV53UpWnzGe/Y/PgpBZZAFwnm2JXoOjuzKs+3CE1KBpxzCf2v2MzQ5dPUCCKSYTfp6k32O8jKNjDNWkai1p3CUKcaQIUPTY59IO6HR8aDLzL933Sgkwhjeu8qvvwvaR/ALW8d7DmGSOY3a+udjeZf+GW2aFvCiXB4=',
    'QueueITAccepted-SDFrts345E-V3_dclprdwr005commerce': 'EventId%3Ddclprdwr005commerce%26QueueId%3D00000000-0000-0000-0000-000000000000%26RedirectType%3Dafterevent%26IssueTime%3D1791012980%26Hash%3D3cebab393b9c62a8539aa05965b811cbc97bf0608aef9c795063acbb0a704187',
    '_abck': '59F36C15B665380E8375DAFB3655B537~-1~YAAQZ/naF9KSKvKgAQAAy0ixABCkqpkyaRkfd8YDoeaUjPWOs1FMIoE9L7LIe8bFuIRhmQL2Jk78VTcb8Z0G+cKnwriHSFOxFjiclM4t9Uq+MeO0l9uwszl8/Dgq+CCrdHKkmn122amCA9gCp1wDPyQQzvY13ymen4SPiYW/Uo2WDbf4ddenpSUjJFh7U9ijLVdSl/7GHkl15mJCAvDwZxXvX4xXX6Rv2/6dT/hQR7L39DOaGzy82PeSU0TAhkJsvsYziDPIw62BSgCUrOVpQ/EBWfQ3SLSX1QI+VhYfGULpVWuHWMoHDvmQHTzKzfTS/azD+11Z9GUJRpvxyF8eHRyrhIV+dw0YyKQfv6CrMUIUJI4gCCCpysx8KNU3D6f64se34y5wm8xWrjU0t2DeZDBk/C34fA6lAP761BWw2eB+CSp42dBFrle2Ewe0Oce2vOBS5tWJXHQ0emG/NR1zy2KNnkWRsG1pKWwov/+gjlTejsbcJvxdH4qtiFnTi9iPYJGjk5nGRzt8FXQJdH5hEZodPX275UgbwZOe8NrAiuCKM2znETcXuCWQlKPw7z5vm4kthJ58E4Bfeo/GLCUjaCZ1Y3tRcaRVljFt3jDgb5BTmT666Vf/sC0IEa6yfq6bueu7+eejeZddEFGIthTmhF4VZEfa4ZOB0Q+PljENxIrfpVz0A9Vs1DAGfiFmVNgRa42YSE7uAdgYHjxDq8vIxuXn9dphF2GyPWaLyi/1bREeNuOZaY6mgWyrShhmznDPSO3W0IFsyB5yqccCotPjO8BzP+3RGyBT7bMN6+wP0QePNbTaCijFhpSGzGqfBxdlwVGsHN7vcxG6ger/MQyuVoBMbfxpfnovw146GoNfFOoBOLLMkpQi9ftp~-1~-1~-1~-1~-1',
    'QueueITAccepted-SDFrts345E-V3_dclprod002': 'EventId%3Ddclprod002%26QueueId%3D72e5170a-3a2e-4d3c-8d27-a58f143a5a04%26RedirectType%3Dsafetynet%26IssueTime%3D1791012981%26Hash%3D071c0cdf929c979a1d9dd69c300a8e1f3665d7b2a1832602b033abf92473faf9',
    'latestWDPROGeoIP': 'eyJhcmVhY29kZSI6IjAiLCJjb3VudHJ5IjoiaW5kaWEiLCJjb250aW5lbnQiOiJhcyIsImNvbm5lY3Rpb24iOiJicm9hZGJhbmQiLCJjb3VudHJ5Y29kZSI6IjM1NiIsImNvdW50cnlpc29jb2RlIjoiaW5kIiwiZG9tYWluIjoiYWVycGFjZS5jb20iLCJkc3QiOiJuIiwiaXNwIjoiY2xvdWQgaW5ub3ZhdGlvbiBsdGQiLCJtZXRybyI6Im5vIG1ldHJvIiwibWV0cm9jb2RlIjoiMCIsIm9mZnNldCI6IjUzMCIsInBvc3Rjb2RlIjoiPyIsInNpYyI6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyIsInNpY2NvZGUiOiI1MTcxMTEiLCJzdGF0ZSI6Im1haGFyYXNodHJhIiwiemlwIjoiMCIsImlwIjoiMTU0Ljg0LjI0OC4xMjkifQ%3D%3D',
    'WDPROGeoIP': 'YToxODp7czo4OiJhcmVhY29kZSI7czoxOiIwIjtzOjc6ImNvdW50cnkiO3M6NToiaW5kaWEiO3M6OToiY29udGluZW50IjtzOjI6ImFzIjtzOjEwOiJjb25uZWN0aW9uIjtzOjk6ImJyb2FkYmFuZCI7czoxMToiY291bnRyeWNvZGUiO3M6MzoiMzU2IjtzOjE0OiJjb3VudHJ5aXNvY29kZSI7czozOiJpbmQiO3M6NjoiZG9tYWluIjtzOjExOiJhZXJwYWNlLmNvbSI7czozOiJkc3QiO3M6MToibiI7czozOiJpc3AiO3M6MjA6ImNsb3VkIGlubm92YXRpb24gbHRkIjtzOjU6Im1ldHJvIjtzOjg6Im5vIG1ldHJvIjtzOjk6Im1ldHJvY29kZSI7czoxOiIwIjtzOjY6Im9mZnNldCI7czozOiI1MzAiO3M6ODoicG9zdGNvZGUiO3M6MToiPyI7czozOiJzaWMiO3M6MzM6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyI7czo3OiJzaWNjb2RlIjtzOjY6IjUxNzExMSI7czo1OiJzdGF0ZSI7czoxMToibWFoYXJhc2h0cmEiO3M6MzoiemlwIjtzOjE6IjAiO3M6MjoiaXAiO3M6MTQ6IjE1NC44NC4yNDguMTI5Ijt9',
    'bm_s': 'YAAQZ/naFxKTKvKgAQAAbkuxAAbCXI+iZlUP9ka/PCaOYCplEhK1oIV65xboflU4KnJS4Dbvpahy8YoiAmpDBAa3fjvAnoD+l6YvjGlyybGhndwMj6oWTLKddY8Uo1lavRwt4uVNEMFIqrdxOKD2PZTrc/rIZVq2rJy0ahEdnFm4jdKNApxByDy8HQ+EIZ2XMVzV2DcS2k5c45kAw+1mlURwJrmxKa6nqtVBMMfJJKVfQ+TUNMFTwpsXWkpaNClke0no4FkifzFTmEgRC51eIO07Rvyyk8UXTgs/9K1f4D0l0Em38B593ihvrQovllSOqQ61RLWd/fJ27bJw+/qorX+qbFh9gbk+1SYuYm66iSoh0LqqthX9TDSuDtikL0eLQhdZ2C0ryC38/DnM8A2kV9VJBaQLAr8HlV0xsJ9dCY+R2qKYB6iVxL15bcIKz+JIiMcBp1cvNM4fUX1IzjfoplPo4wuQjq44xgsy/6E86Ekv7WxP2dsLrv+5H4rqEdweSjfFiv85nryt3iX/dwYALL6Hd/9z63eiS1j1qTLzdT+quoJ8GxIIBGvRXTDoe37+zxX3WrBcisLHYgsXXRIB8T17Al1fm18B8JE6urEV6xgBnsdfrkEZelzZjbMFGqTr9IVsXDr4Iu3HFf+vk5PUaUM8U+FfQ+wXS3DX3h0X9yFk3itsLzIcvSBrs3Suc8UTvLfYhw180W6uk+Db24PQhNqkrEj1YyKOZ3VJw8dFk9w3gffUZPNywmmBvtytvXv70QUpvYvOlBSCE3+C+i5GcmDcMkxIzaXWMsCjXJOAlNkbn6AJ1Y0gB/W2y86JLlQi3oUxFDJPVCgs1RI2C/IG+KonuyJGUKl3i9M61TGE8WtInFjw7y4r3UdSylKxQ67RSIy+r+CnUMQYipApyTQ1Uqhk0tyI1C0RIrw60on6gb8nHXMpe7GzW67h1uaKcTszomnZ4DTXfYPS4KfCuSKkgqHgOHt94sufnQe6zHrNW5CXVRYazP3+euPMZgSV3nOI4hjshfMOTlUmed5W725CO32Iw2rTLKhl3dHxjQlmgB6UYIA1b+wvkzkqrJSzESRdi+vZisLO+2Qter0SZWiD0LnNVkLMFjlvSGDso4R8+iM=',
    'bm_sz': '6A1F38E22EB4158680F98466F6311E35~YAAQZ/naFxOTKvKgAQAAbkuxAAH6mrd60GjuigJ0c7gnZwblvegt3kO4B+2YUntQ9UibLRW9o90BX04xMv83Ni8+9JRdQm7EvJfsMktJqLCj9iDeulfbYaIprOASnu2FRfa+eKdLUtdDImVKCWhPMZXFoQ/xmRUYOIdRcUVnjNBDAoFc3x0WyV7e9YLbOPpjUhyzn6pyjk1m0Dh9TOIPDQPuSla8hKSk2oraIBt4XkL9PP7K1QEMbeTaigVkzl+9ElsOuze3sA8KpTIob6oEuueqY3YiKbxFWrD7YSpADsdmBoA6jib6w7v+fjYi2pnhWZ2//rHLwpd1sTiZCqKUVXdkCqNmi1HqmRxAO8gb2NTJekwQnI8+AHfMRRWECjLCwbSZMJu3/NhK26y8KkPThC9ID7AoGw5hDfm8PPxVqE0GLY3UxNeaD62FR+bbL3/FLORhGKY9~3228211~4338232',
    'surveyThreshold_jar': '%7B%22pageViewThreshold%22%3A2%7D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Oct+03+2026+13%3A06%3A26+GMT%2B0530+(India+Standard+Time)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=IdentityId&hosts=&consentId=c300b578-9418-4b1c-b71d-8f84295f47a5&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=BG618%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false',
    'WDPROView': '%7B%22version%22%3A2%2C%22deviceInfo%22%3A%7B%22device%22%3A%22mobile%22%2C%22os%22%3A%22androidos%22%7D%2C%22preferred%22%3A%7B%22device%22%3A%22mobile%22%7D%2C%22browserInfo%22%3A%7B%22agent%22%3A%22Chrome%22%2C%22version%22%3A154%7D%7D',
    'geoipLegacy': 'eyJhcmVhY29kZSI6IjAiLCJjb3VudHJ5IjoiaW5kaWEiLCJjb250aW5lbnQiOiJhcyIsImNvbm5lY3Rpb24iOiJicm9hZGJhbmQiLCJjb3VudHJ5Y29kZSI6IjM1NiIsImNvdW50cnlpc29jb2RlIjoiaW5kIiwiZG9tYWluIjoiYWVycGFjZS5jb20iLCJkc3QiOiJuIiwiaXNwIjoiY2xvdWQgaW5ub3ZhdGlvbiBsdGQiLCJtZXRybyI6Im5vIG1ldHJvIiwibWV0cm9jb2RlIjoiMCIsIm9mZnNldCI6IjUzMCIsInBvc3Rjb2RlIjoiPyIsInNpYyI6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyIsInNpY2NvZGUiOiI1MTcxMTEiLCJzdGF0ZSI6Im1haGFyYXNodHJhIiwiemlwIjoiMCIsImlwIjoiMTU0Ljg0LjI0OC4xMjkifQ%3D%3D',
    'geoip': 'YToxODp7czo4OiJhcmVhY29kZSI7czoxOiIwIjtzOjc6ImNvdW50cnkiO3M6NToiaW5kaWEiO3M6OToiY29udGluZW50IjtzOjI6ImFzIjtzOjEwOiJjb25uZWN0aW9uIjtzOjk6ImJyb2FkYmFuZCI7czoxMToiY291bnRyeWNvZGUiO3M6MzoiMzU2IjtzOjE0OiJjb3VudHJ5aXNvY29kZSI7czozOiJpbmQiO3M6NjoiZG9tYWluIjtzOjExOiJhZXJwYWNlLmNvbSI7czozOiJkc3QiO3M6MToibiI7czozOiJpc3AiO3M6MjA6ImNsb3VkIGlubm92YXRpb24gbHRkIjtzOjU6Im1ldHJvIjtzOjg6Im5vIG1ldHJvIjtzOjk6Im1ldHJvY29kZSI7czoxOiIwIjtzOjY6Im9mZnNldCI7czozOiI1MzAiO3M6ODoicG9zdGNvZGUiO3M6MToiPyI7czozOiJzaWMiO3M6MzM6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyI7czo3OiJzaWNjb2RlIjtzOjY6IjUxNzExMSI7czo1OiJzdGF0ZSI7czoxMToibWFoYXJhc2h0cmEiO3M6MzoiemlwIjtzOjE6IjAiO3M6MjoiaXAiO3M6MTQ6IjE1NC44NC4yNDguMTI5Ijt9Ow%3D%3D',
    'connect.sid': 's%3A65ZH1OzDzN6ti55iNcbEDLL5mdg7CE5u.4dKVaLXW1SdLBWoc85HvL16iIll73%2BMgC7tMqQjV2t8',
    'bm_sv': 'A52722D2EE295F44E8F8B2B4EA8AED5B~YAAQZ/naF3buKvKgAQAAye22AAH+MtnuMvn3JHJDECJKClOWkc0DZSz3lDtbMz2Tivh/NmS+jTjzZp0GT4nBVAaRv+Qtu6lM7Ojyyq9QqXerLYod0ksACzAqYCvGVrKFIOoRUNS77Gm/5gc4sMuVog92RUs4+kLnthW6Ell/oQ71UexoYqKSN/JYTR0bvL5CkSyCOB6SKmbsHQMbooc4ZYwYaP97x2cjqt1ELQ9owQ4Vg1TC+yyxxMAl+s1nzA63JQnkSg==~1',
    'Conversation_UUID': 'b25aac66-9821-417e-8801-858654677541',
    's_pers': '%20s_gpv_pn%3Dwdpro%252Fdcl%252Fin%252Fen%252Fcommerce%252Fbooking%252Fconsumer%252Fsearchresults%7C1791015762961%3B',
    's_sess': '%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_tp%3D1345%3B%20s_slt%3D%3B%20s_ppv%3Dwdpro%252Fdcl%252Fin%252Fen%252Fcommerce%252Fbooking%252Fconsumer%252Fsearchresults%252C72%252C72%252C968%3B',
    'mbox': 'session#6f5c0b47885048a89624f6bfb5586173#1791015824|PC#6f5c0b47885048a89624f6bfb5586173.41_0#1854258764',
}

HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-in',
    'content-type': 'application/json',
    'origin': 'https://disneycruise.disney.go.com',
    'priority': 'u=1, i',
    'referer': 'https://disneycruise.disney.go.com/en-in/cruises-destinations/list',
    'sec-ch-ua': '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 16; Pixel 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Mobile Safari/537.36',
    'x-bypass-product-avail-svc': 'false',
    'x-conversation-id': 'b25aac66-9821-417e-8801-858654677541',
    'x-correlation-id': 'b8db94c9-6699-442e-a34d-d61beaef0d75',
    'x-disney-internal-is-cast': 'false',
    'x-page-id': 'https://disneycruise.disney.go.com/en-in/cruises-destinations/list',
    'x-use-voyage-svc': 'true',
    # 'cookie': 'geolocation_aka_jar=%7B%22zipCode%22%3A%22%22%2C%22region%22%3A%22MH%22%2C%22country%22%3A%22IN%22%2C%22metro%22%3A%22CHINCHVAD%22%2C%22metroCode%22%3A%22%22%7D; bm_so=C69D5A8ED547496333990D5057735A2BAD55C22BA64BFBCC6391C6E8385E5AC3~YAAQZ/naFzFqKvKgAQAA8cGuAAnUU6zBP5IrMC5FpK8cUoI2YRiQKf2EcxWt4a8GIfRUK/PnglIupNmx7jqVyKtAaPsPzToMUZk+BiWE+VqdKi/cjPwWTsGdeeX/9M7iq4Ho291oSXwyGKccLM77E/tX98z9XxJEpAB2Xh/7kaGYUlXpwzWMsaBmIfZxOi4pggA9Y0AlptLowLMG7vJcpaFYd1Txa4vLFRAdakdf5BUC7ann+WOmSyfJdIQGHAaCA9CVDthnKWEayz+2Qt53nT7edDZIUOj/0XJRx1B/SYeDrTPYWGjnk+l9PHCuc6JTIDQj06Ic+yWCB4YBEdrzepIXBzRAK+mRoBnuIDhPNCW7R47YI2zQt/E4GVgKNnOhtK7N0cn8SmXcu4wcbZpDSdaDlUrRJxFJh0lKoarGdLwFHL66stjK2eFIWkrC6/gE8ZsCFZirmKvNB9RDx2WCKEQcsW8zsaqi~4; siteId=dcl; localeCookie_jar_aka=%7B%22contentLocale%22%3A%22en_IN%22%2C%22version%22%3A%222%22%2C%22precedence%22%3A0%2C%22akamai%22%3A%22true%22%2C%22localeCurrency%22%3A%22INR%22%2C%22preferredRegion%22%3A%22en-in%22%7D; languageSelection_jar_aka=%7B%22preferredLanguage%22%3A%22en_IN%22%2C%22version%22%3A%223%22%2C%22precedence%22%3A0%2C%22language%22%3A%22en_IN%22%2C%22akamai%22%3A%22true%22%7D; _cs_mk_aa=0.06718367270832759_1791012816035; bm_lso=C69D5A8ED547496333990D5057735A2BAD55C22BA64BFBCC6391C6E8385E5AC3~YAAQZ/naFzFqKvKgAQAA8cGuAAnUU6zBP5IrMC5FpK8cUoI2YRiQKf2EcxWt4a8GIfRUK/PnglIupNmx7jqVyKtAaPsPzToMUZk+BiWE+VqdKi/cjPwWTsGdeeX/9M7iq4Ho291oSXwyGKccLM77E/tX98z9XxJEpAB2Xh/7kaGYUlXpwzWMsaBmIfZxOi4pggA9Y0AlptLowLMG7vJcpaFYd1Txa4vLFRAdakdf5BUC7ann+WOmSyfJdIQGHAaCA9CVDthnKWEayz+2Qt53nT7edDZIUOj/0XJRx1B/SYeDrTPYWGjnk+l9PHCuc6JTIDQj06Ic+yWCB4YBEdrzepIXBzRAK+mRoBnuIDhPNCW7R47YI2zQt/E4GVgKNnOhtK7N0cn8SmXcu4wcbZpDSdaDlUrRJxFJh0lKoarGdLwFHL66stjK2eFIWkrC6/gE8ZsCFZirmKvNB9RDx2WCKEQcsW8zsaqi~4~1791012816579; PHPSESSID=h9e5iiiap3u1hdjtj0cbkbls13; SWID=9bf9849f-914e-4411-bbfb-c1a0aad35e2c; __pa=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3OTEwMTI4MTgsImFjY2Vzc190b2tlbiI6ImE2YmI2NzRmM2FjNTRmNTRiYWY1YTk3MWZhNWQ4NDkyIiwidG9rZW5fdHlwZSI6IkJFQVJFUiIsImV4cGlyZXNfaW4iOiIyODgwMCJ9.RQFuHV33Wx89Mn90PuwN5gGDTBBn1lGiRAro4TrhxSjkkvPVBL0Zi3TtjwttOnqoyd-Gw2BtXajb9C_HWXF7VQ; paPublicTokenExpireTime=1791041558011; at_check=true; AMCVS_EDA101AC512D2B230A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C57767953894060163791269542447300747941; AMCV_EDA101AC512D2B230A490D4C%40AdobeOrg=-219703956%7CMCIDTS%7C20730%7CMCMID%7C57767953894060163791269542447300747941%7CMCAAMLH-1791617618%7C12%7CMCAAMB-1791617618%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1791020018s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; mboxEdgeCluster=41; kndctr_EDA101AC512D2B230A490D4C_AdobeOrg_identity=CiY1Nzc2Nzk1Mzg5NDA2MDE2Mzc5MTI2OTU0MjQ0NzMwMDc0Nzk0MVIRCK2hu4WQNBgBKgRJTkQxMAPwAa2hu4WQNA==; kndctr_EDA101AC512D2B230A490D4C_AdobeOrg_cluster=ind1; _fbp=fb.1.1791012818979.98616861979130515; _gcl_au=1.1.1246652143.1791012821; ak_bmsc=549D2C7DF47D0EA564257DF032166452~000000000000000000000000000000~YAAQZ/naFxaSKvKgAQAAjT6xAAGp7dMz2EyVE1Jt6wJKD8niCJTrW2bhUH042deq32E4p/oNJpxTGuV/a5BjTP4kJIJq9x1z62RUSziViGPtOErDIaOZV5BDJULsmrL+Q67jlFWvnOyUf08MHxrZWKxuVWtF9v65i2iT6FxP7cAuBA1nUIx/sRTGgdOsHBjhis5eoX3mxOcUeVuOHWWl4k7SXAFHl/o/vMMDr8+mQvPlPxNOUX65CwpwMKwIFIcGDX4hCnI1mQlV53UpWnzGe/Y/PgpBZZAFwnm2JXoOjuzKs+3CE1KBpxzCf2v2MzQ5dPUCCKSYTfp6k32O8jKNjDNWkai1p3CUKcaQIUPTY59IO6HR8aDLzL933Sgkwhjeu8qvvwvaR/ALW8d7DmGSOY3a+udjeZf+GW2aFvCiXB4=; QueueITAccepted-SDFrts345E-V3_dclprdwr005commerce=EventId%3Ddclprdwr005commerce%26QueueId%3D00000000-0000-0000-0000-000000000000%26RedirectType%3Dafterevent%26IssueTime%3D1791012980%26Hash%3D3cebab393b9c62a8539aa05965b811cbc97bf0608aef9c795063acbb0a704187; _abck=59F36C15B665380E8375DAFB3655B537~-1~YAAQZ/naF9KSKvKgAQAAy0ixABCkqpkyaRkfd8YDoeaUjPWOs1FMIoE9L7LIe8bFuIRhmQL2Jk78VTcb8Z0G+cKnwriHSFOxFjiclM4t9Uq+MeO0l9uwszl8/Dgq+CCrdHKkmn122amCA9gCp1wDPyQQzvY13ymen4SPiYW/Uo2WDbf4ddenpSUjJFh7U9ijLVdSl/7GHkl15mJCAvDwZxXvX4xXX6Rv2/6dT/hQR7L39DOaGzy82PeSU0TAhkJsvsYziDPIw62BSgCUrOVpQ/EBWfQ3SLSX1QI+VhYfGULpVWuHWMoHDvmQHTzKzfTS/azD+11Z9GUJRpvxyF8eHRyrhIV+dw0YyKQfv6CrMUIUJI4gCCCpysx8KNU3D6f64se34y5wm8xWrjU0t2DeZDBk/C34fA6lAP761BWw2eB+CSp42dBFrle2Ewe0Oce2vOBS5tWJXHQ0emG/NR1zy2KNnkWRsG1pKWwov/+gjlTejsbcJvxdH4qtiFnTi9iPYJGjk5nGRzt8FXQJdH5hEZodPX275UgbwZOe8NrAiuCKM2znETcXuCWQlKPw7z5vm4kthJ58E4Bfeo/GLCUjaCZ1Y3tRcaRVljFt3jDgb5BTmT666Vf/sC0IEa6yfq6bueu7+eejeZddEFGIthTmhF4VZEfa4ZOB0Q+PljENxIrfpVz0A9Vs1DAGfiFmVNgRa42YSE7uAdgYHjxDq8vIxuXn9dphF2GyPWaLyi/1bREeNuOZaY6mgWyrShhmznDPSO3W0IFsyB5yqccCotPjO8BzP+3RGyBT7bMN6+wP0QePNbTaCijFhpSGzGqfBxdlwVGsHN7vcxG6ger/MQyuVoBMbfxpfnovw146GoNfFOoBOLLMkpQi9ftp~-1~-1~-1~-1~-1; QueueITAccepted-SDFrts345E-V3_dclprod002=EventId%3Ddclprod002%26QueueId%3D72e5170a-3a2e-4d3c-8d27-a58f143a5a04%26RedirectType%3Dsafetynet%26IssueTime%3D1791012981%26Hash%3D071c0cdf929c979a1d9dd69c300a8e1f3665d7b2a1832602b033abf92473faf9; latestWDPROGeoIP=eyJhcmVhY29kZSI6IjAiLCJjb3VudHJ5IjoiaW5kaWEiLCJjb250aW5lbnQiOiJhcyIsImNvbm5lY3Rpb24iOiJicm9hZGJhbmQiLCJjb3VudHJ5Y29kZSI6IjM1NiIsImNvdW50cnlpc29jb2RlIjoiaW5kIiwiZG9tYWluIjoiYWVycGFjZS5jb20iLCJkc3QiOiJuIiwiaXNwIjoiY2xvdWQgaW5ub3ZhdGlvbiBsdGQiLCJtZXRybyI6Im5vIG1ldHJvIiwibWV0cm9jb2RlIjoiMCIsIm9mZnNldCI6IjUzMCIsInBvc3Rjb2RlIjoiPyIsInNpYyI6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyIsInNpY2NvZGUiOiI1MTcxMTEiLCJzdGF0ZSI6Im1haGFyYXNodHJhIiwiemlwIjoiMCIsImlwIjoiMTU0Ljg0LjI0OC4xMjkifQ%3D%3D; WDPROGeoIP=YToxODp7czo4OiJhcmVhY29kZSI7czoxOiIwIjtzOjc6ImNvdW50cnkiO3M6NToiaW5kaWEiO3M6OToiY29udGluZW50IjtzOjI6ImFzIjtzOjEwOiJjb25uZWN0aW9uIjtzOjk6ImJyb2FkYmFuZCI7czoxMToiY291bnRyeWNvZGUiO3M6MzoiMzU2IjtzOjE0OiJjb3VudHJ5aXNvY29kZSI7czozOiJpbmQiO3M6NjoiZG9tYWluIjtzOjExOiJhZXJwYWNlLmNvbSI7czozOiJkc3QiO3M6MToibiI7czozOiJpc3AiO3M6MjA6ImNsb3VkIGlubm92YXRpb24gbHRkIjtzOjU6Im1ldHJvIjtzOjg6Im5vIG1ldHJvIjtzOjk6Im1ldHJvY29kZSI7czoxOiIwIjtzOjY6Im9mZnNldCI7czozOiI1MzAiO3M6ODoicG9zdGNvZGUiO3M6MToiPyI7czozOiJzaWMiO3M6MzM6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyI7czo3OiJzaWNjb2RlIjtzOjY6IjUxNzExMSI7czo1OiJzdGF0ZSI7czoxMToibWFoYXJhc2h0cmEiO3M6MzoiemlwIjtzOjE6IjAiO3M6MjoiaXAiO3M6MTQ6IjE1NC44NC4yNDguMTI5Ijt9; bm_s=YAAQZ/naFxKTKvKgAQAAbkuxAAbCXI+iZlUP9ka/PCaOYCplEhK1oIV65xboflU4KnJS4Dbvpahy8YoiAmpDBAa3fjvAnoD+l6YvjGlyybGhndwMj6oWTLKddY8Uo1lavRwt4uVNEMFIqrdxOKD2PZTrc/rIZVq2rJy0ahEdnFm4jdKNApxByDy8HQ+EIZ2XMVzV2DcS2k5c45kAw+1mlURwJrmxKa6nqtVBMMfJJKVfQ+TUNMFTwpsXWkpaNClke0no4FkifzFTmEgRC51eIO07Rvyyk8UXTgs/9K1f4D0l0Em38B593ihvrQovllSOqQ61RLWd/fJ27bJw+/qorX+qbFh9gbk+1SYuYm66iSoh0LqqthX9TDSuDtikL0eLQhdZ2C0ryC38/DnM8A2kV9VJBaQLAr8HlV0xsJ9dCY+R2qKYB6iVxL15bcIKz+JIiMcBp1cvNM4fUX1IzjfoplPo4wuQjq44xgsy/6E86Ekv7WxP2dsLrv+5H4rqEdweSjfFiv85nryt3iX/dwYALL6Hd/9z63eiS1j1qTLzdT+quoJ8GxIIBGvRXTDoe37+zxX3WrBcisLHYgsXXRIB8T17Al1fm18B8JE6urEV6xgBnsdfrkEZelzZjbMFGqTr9IVsXDr4Iu3HFf+vk5PUaUM8U+FfQ+wXS3DX3h0X9yFk3itsLzIcvSBrs3Suc8UTvLfYhw180W6uk+Db24PQhNqkrEj1YyKOZ3VJw8dFk9w3gffUZPNywmmBvtytvXv70QUpvYvOlBSCE3+C+i5GcmDcMkxIzaXWMsCjXJOAlNkbn6AJ1Y0gB/W2y86JLlQi3oUxFDJPVCgs1RI2C/IG+KonuyJGUKl3i9M61TGE8WtInFjw7y4r3UdSylKxQ67RSIy+r+CnUMQYipApyTQ1Uqhk0tyI1C0RIrw60on6gb8nHXMpe7GzW67h1uaKcTszomnZ4DTXfYPS4KfCuSKkgqHgOHt94sufnQe6zHrNW5CXVRYazP3+euPMZgSV3nOI4hjshfMOTlUmed5W725CO32Iw2rTLKhl3dHxjQlmgB6UYIA1b+wvkzkqrJSzESRdi+vZisLO+2Qter0SZWiD0LnNVkLMFjlvSGDso4R8+iM=; bm_sz=6A1F38E22EB4158680F98466F6311E35~YAAQZ/naFxOTKvKgAQAAbkuxAAH6mrd60GjuigJ0c7gnZwblvegt3kO4B+2YUntQ9UibLRW9o90BX04xMv83Ni8+9JRdQm7EvJfsMktJqLCj9iDeulfbYaIprOASnu2FRfa+eKdLUtdDImVKCWhPMZXFoQ/xmRUYOIdRcUVnjNBDAoFc3x0WyV7e9YLbOPpjUhyzn6pyjk1m0Dh9TOIPDQPuSla8hKSk2oraIBt4XkL9PP7K1QEMbeTaigVkzl+9ElsOuze3sA8KpTIob6oEuueqY3YiKbxFWrD7YSpADsdmBoA6jib6w7v+fjYi2pnhWZ2//rHLwpd1sTiZCqKUVXdkCqNmi1HqmRxAO8gb2NTJekwQnI8+AHfMRRWECjLCwbSZMJu3/NhK26y8KkPThC9ID7AoGw5hDfm8PPxVqE0GLY3UxNeaD62FR+bbL3/FLORhGKY9~3228211~4338232; surveyThreshold_jar=%7B%22pageViewThreshold%22%3A2%7D; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Oct+03+2026+13%3A06%3A26+GMT%2B0530+(India+Standard+Time)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=IdentityId&hosts=&consentId=c300b578-9418-4b1c-b71d-8f84295f47a5&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=BG618%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; WDPROView=%7B%22version%22%3A2%2C%22deviceInfo%22%3A%7B%22device%22%3A%22mobile%22%2C%22os%22%3A%22androidos%22%7D%2C%22preferred%22%3A%7B%22device%22%3A%22mobile%22%7D%2C%22browserInfo%22%3A%7B%22agent%22%3A%22Chrome%22%2C%22version%22%3A154%7D%7D; geoipLegacy=eyJhcmVhY29kZSI6IjAiLCJjb3VudHJ5IjoiaW5kaWEiLCJjb250aW5lbnQiOiJhcyIsImNvbm5lY3Rpb24iOiJicm9hZGJhbmQiLCJjb3VudHJ5Y29kZSI6IjM1NiIsImNvdW50cnlpc29jb2RlIjoiaW5kIiwiZG9tYWluIjoiYWVycGFjZS5jb20iLCJkc3QiOiJuIiwiaXNwIjoiY2xvdWQgaW5ub3ZhdGlvbiBsdGQiLCJtZXRybyI6Im5vIG1ldHJvIiwibWV0cm9jb2RlIjoiMCIsIm9mZnNldCI6IjUzMCIsInBvc3Rjb2RlIjoiPyIsInNpYyI6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyIsInNpY2NvZGUiOiI1MTcxMTEiLCJzdGF0ZSI6Im1haGFyYXNodHJhIiwiemlwIjoiMCIsImlwIjoiMTU0Ljg0LjI0OC4xMjkifQ%3D%3D; geoip=YToxODp7czo4OiJhcmVhY29kZSI7czoxOiIwIjtzOjc6ImNvdW50cnkiO3M6NToiaW5kaWEiO3M6OToiY29udGluZW50IjtzOjI6ImFzIjtzOjEwOiJjb25uZWN0aW9uIjtzOjk6ImJyb2FkYmFuZCI7czoxMToiY291bnRyeWNvZGUiO3M6MzoiMzU2IjtzOjE0OiJjb3VudHJ5aXNvY29kZSI7czozOiJpbmQiO3M6NjoiZG9tYWluIjtzOjExOiJhZXJwYWNlLmNvbSI7czozOiJkc3QiO3M6MToibiI7czozOiJpc3AiO3M6MjA6ImNsb3VkIGlubm92YXRpb24gbHRkIjtzOjU6Im1ldHJvIjtzOjg6Im5vIG1ldHJvIjtzOjk6Im1ldHJvY29kZSI7czoxOiIwIjtzOjY6Im9mZnNldCI7czozOiI1MzAiO3M6ODoicG9zdGNvZGUiO3M6MToiPyI7czozOiJzaWMiO3M6MzM6IldpcmVkIFRlbGVjb21tdW5pY2F0aW9ucyBDYXJyaWVycyI7czo3OiJzaWNjb2RlIjtzOjY6IjUxNzExMSI7czo1OiJzdGF0ZSI7czoxMToibWFoYXJhc2h0cmEiO3M6MzoiemlwIjtzOjE6IjAiO3M6MjoiaXAiO3M6MTQ6IjE1NC44NC4yNDguMTI5Ijt9Ow%3D%3D; connect.sid=s%3A65ZH1OzDzN6ti55iNcbEDLL5mdg7CE5u.4dKVaLXW1SdLBWoc85HvL16iIll73%2BMgC7tMqQjV2t8; bm_sv=A52722D2EE295F44E8F8B2B4EA8AED5B~YAAQZ/naF3buKvKgAQAAye22AAH+MtnuMvn3JHJDECJKClOWkc0DZSz3lDtbMz2Tivh/NmS+jTjzZp0GT4nBVAaRv+Qtu6lM7Ojyyq9QqXerLYod0ksACzAqYCvGVrKFIOoRUNS77Gm/5gc4sMuVog92RUs4+kLnthW6Ell/oQ71UexoYqKSN/JYTR0bvL5CkSyCOB6SKmbsHQMbooc4ZYwYaP97x2cjqt1ELQ9owQ4Vg1TC+yyxxMAl+s1nzA63JQnkSg==~1; Conversation_UUID=b25aac66-9821-417e-8801-858654677541; s_pers=%20s_gpv_pn%3Dwdpro%252Fdcl%252Fin%252Fen%252Fcommerce%252Fbooking%252Fconsumer%252Fsearchresults%7C1791015762961%3B; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_tp%3D1345%3B%20s_slt%3D%3B%20s_ppv%3Dwdpro%252Fdcl%252Fin%252Fen%252Fcommerce%252Fbooking%252Fconsumer%252Fsearchresults%252C72%252C72%252C968%3B; mbox=session#6f5c0b47885048a89624f6bfb5586173#1791015824|PC#6f5c0b47885048a89624f6bfb5586173.41_0#1854258764',
}

json_data = {
    'currency': 'INR',
    'filters': [],
    'partyMix': [
        {
            'accessible': False,
            'adultCount': 2,
            'childCount': 0,
            'nonAdultAges': [],
            'partyMixId': '0',
        },
    ],
    'region': 'INTL',
    'storeId': 'DCL',
    'affiliations': [],
    'page': 1,
    'pageHistory': False,
    'includeAdvancedBookingPrices': True,
    'exploreMorePage': 1,
    'exploreMorePageHistory': False,
    'sorts': [
        {
            'criteria': 'RECOMMENDED',
            'order': 'ASC',
            'region': 'MH',
        },
    ],
}



# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"currency":"INR","filters":[],"partyMix":[{"accessible":false,"adultCount":2,"childCount":0,"nonAdultAges":[],"partyMixId":"0"}],"region":"INTL","storeId":"DCL","affiliations":[],"page":1,"pageHistory":false,"includeAdvancedBookingPrices":true,"exploreMorePage":1,"exploreMorePageHistory":false,"sorts":[{"criteria":"RECOMMENDED","order":"ASC","region":"MH"}]}'
#response = requests.post(
#    'https://disneycruise.disney.go.com/dcl-apps-productavail-vas/available-products/',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

def scrape_disney_api():
    all_cruises = []
    
    # Challenge requires fetching at least 35 pages
    for current_page in range(1, 36):
        print(f"Fetching Page {current_page} of 35...")
        
        # We update the payload dynamically for each page
        payload = {
            "currency": "INR",
            "filters": [],
            "partyMix": [{"accessible": False, "adultCount": 2, "childCount": 0, "nonAdultAges": [], "partyMixId": "0"}],
            "region": "INTL",
            "storeId": "DCL",
            "affiliations": [],
            "page": current_page, # <--- PAGINATION INJECTED HERE
            "pageHistory": False,
            "includeAdvancedBookingPrices": True,
            "exploreMorePage": 1,
            "exploreMorePageHistory": False,
            "sorts": [{"criteria": "RECOMMENDED", "order": "ASC", "region": "MH"}]
        }

        try:
            response = requests.post(
                'https://disneycruise.disney.go.com/dcl-apps-productavail-vas/available-products/',
                cookies=COOKIES,
                headers=HEADERS,
                json=payload,
                timeout=15
            )
            response.raise_for_status()
            data = response.json()
            
            # The JSON snippet confirms the list is called 'products'
            products = data.get('products', [])
            
            if not products:
                print("No more products found. Exiting loop.")
                break
                
            for item in products:
                # 1. Grab the exact title
                title = item.get('productName', 'N/A')
                
                # 2. Dig into the 'itineraries' array to sum up the total available dates
                itineraries = item.get('itineraries', [])
                dates_count = sum(itin.get('numberOfSailings', 0) for itin in itineraries)
                
                # 3. Clean and extract data directly from the Title string
                # Splits "3-Night Cruise from Singapore" to get "Singapore"
                departing_from = title.split(' from ')[-1] if ' from ' in title else 'N/A'
                duration = title.split(' ')[0] if '-Night' in title else 'N/A'
                
                all_cruises.append({
                    "Title": title,
                    "Departing From": departing_from,
                    "Duration": duration,
                    "Destination": title, # Title contains the destination keywords (Pacific, Baja, etc.)
                    "Available_Dates_Count": dates_count
                })
                
        except Exception as e:
            print(f"Error on page {current_page}: {e}")
            
        time.sleep(1.5) # Prevent rate-limiting
        
    return all_cruises

def clean_and_calculate(raw_data):
    df = pd.DataFrame(raw_data)
    
    # STEP 5: Data Cleaning Rules
    # 1. Ensure locations are present and not empty
    df = df[df['Departing From'] != '']
    df = df.dropna(subset=['Departing From'])
    
    # 2. Ensure no duplicate data is present
    df = df.drop_duplicates(subset=['Title', 'Departing From', 'Duration'])
    
    # Save the cleaned CSV
    csv_filename = "Disney_Cruise_Results.csv"
    df.to_csv(csv_filename, index=False)
    print(f"\nSaved {len(df)} clean records to {csv_filename}")
    
    # HACKATHON REQUIRED TERMINAL OUTPUT
    print("\n--- HACKATHON QUESTION ANSWERS ---")
    
    # Q1: Total cruises for the Pacific as a destination
    pacific_cruises = df[df['Destination'].str.contains('Pacific', case=False, na=False)].shape[0]
    print(f"(i) Total Pacific cruises: {pacific_cruises}")
    
    # Q2: How many total cruises are there?
    print(f"(ii) Total cruises: {len(df)}")
    
    # Q3: How many holiday cruises are there? (Look for Merrytime/Holiday keywords)
    holiday_cruises = df[df['Title'].str.contains('Merrytime|Holiday|Halloween', case=False, na=False)].shape[0]
    print(f"(iii) Total holiday cruises: {holiday_cruises}")
    
    # Q4: How many Cruises offer more than 2 dates for booking?
    multi_date_cruises = df[df['Available_Dates_Count'] > 2].shape[0]
    print(f"(iv) Cruises with >2 dates: {multi_date_cruises}")
    
    # Q5: How many cruises do Miami and London have as departure ports?
    miami_london = df[df['Departing From'].str.contains('Miami|London', case=False, na=False)].shape[0]
    print(f"(v) Cruises departing from Miami/London: {miami_london}")

# Execution
if __name__ == "__main__":
    extracted_data = scrape_disney_api()
    if extracted_data:
        clean_and_calculate(extracted_data)