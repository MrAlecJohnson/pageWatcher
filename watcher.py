from bs4 import BeautifulSoup
from datetime import date
import requests
import json
import flask

# Pages to scrape
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

def getContent(url):
    """Reads a Gov page, finds + tidies the main content 
    Returns a json-ready dict including today's date"""
    address = requests.get(url)
    html = address.text
    soup = BeautifulSoup(html, 'lxml') 
    page = soup.main.div.find_all(class_ = ["column-two-thirds", "govuk-grid-column-two-thirds"])[1]
    part = page.h1.text.replace('\n\n','\n')
    content = page.div.text.strip()
    return {'url': url, 
            'heading': part, 
            'content': content.strip(), 
            'date': str(date.today()), 
            'dateStr': str(date.today().strftime('%-d %B %Y'))}

def start(file, pagelist):
    """When running for first time, create json of current content"""
    current = []
    for url in pagelist: 
        content = getContent(url)
        current.append(content)
    
    with open(file, "w") as f:
        json.dump(current, f, default = str)

def update(file, pagelist):
    """To update, grab the pages and check if they've changed
    If they have, replace the content stored in json and update the date
    Not yet trying to identify what's changed - just whether something has"""
    current = []
    for url in pagelist: 
        content = getContent(url)
        current.append(content)    
    
    with open(file, "r") as f:
        previous = json.load(f)
    
    for i in range(len(current)):
        if current[i]['content'] != previous[i]['content']:
            previous[i] = current[i]
            
    with open(file, "w") as f:
        json.dump(previous, f, default = str)

# %%

app = flask.Flask(__name__)

start('content.json', pageList)

@app.route('/index', methods = ["GET"])
def index():
    with open('content.json', "r") as f:
        table = json.load(f)

    return flask.render_template('watcher.html',
                                 pageTable = table)
                                 
if __name__ == '__main__':
    app.run(debug = True, port = 5001)

