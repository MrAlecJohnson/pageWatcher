import json
from watcher import pageList, getContent

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
                                 
if __name__ == '__main__':
    update('content.json', pageList)

