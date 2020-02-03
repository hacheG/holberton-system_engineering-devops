#!/usr/bin/python3
"""a day more for die"""

import requests
from sys import argv

if __name__ == "__main__":

    numTaskCompĺete = 0
    theNumId = argv[1]
    
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(theNumId))
    showJson = r.json()
    oneId = showJson.get('username')

    r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(theNumId))
    showJson2 = r2.json()

    theNumId = int(theNumId)
    for json in showJson2:
        if json.get('userId') == theNumId:
            theUserId = json.get('userId')
            completedTF = json.get('completed')
            theTitle = json.get('title')
            if json.get('completed') is not None:
                file = open("{}.csv".format(theNumId), "a")
                file.write('"{}","{}","{}","{}"\n'.format(theUserId, oneId, completedTF, theTitle))
  
    file.close()

