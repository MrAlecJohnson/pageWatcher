from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json

pageList = ["https://www.gov.uk/settled-status-eu-citizens-families",
            "https://www.gov.uk/settled-status-eu-citizens-families/eligibility",
            "https://www.gov.uk/settled-status-eu-citizens-families/what-settled-and-presettled-status-means",
            "https://www.gov.uk/settled-status-eu-citizens-families/what-youll-need-to-apply",
            "https://www.gov.uk/settled-status-eu-citizens-families/applying-for-settled-status",
            "https://www.gov.uk/settled-status-eu-citizens-families/not-EU-EEA-Swiss-citizen",
            "https://www.gov.uk/settled-status-eu-citizens-families/if-you-have-permanent-residence-or-indefinite-leave-to-remain",
            "https://www.gov.uk/settled-status-eu-citizens-families/apply-settled-status-for-child",
            "https://www.gov.uk/settled-status-eu-citizens-families/settled-status-less-than-5-years",
            "https://www.gov.uk/settled-status-eu-citizens-families/after-youve-applied"]


# %%

def getContent(url):
    address = requests.get(url)
    html = address.text
    soup = BeautifulSoup(html, 'lxml') 
    title = soup.title.text
    page = soup.main.div.find_all(class_ = ["column-two-thirds", "govuk-grid-column-two-thirds"])[1]
    part = page.h1.text
    content = page.div.text
    return {'url': url, 'heading': part, 'content': content}

# %%
    
current = []
for url in pageList: 
    content = getContent(url)
    current.append(content)
    
"""with open("current.json", "w") as write_file:
    json.dump(current, write_file)"""

previous = 
        
#%%
        
