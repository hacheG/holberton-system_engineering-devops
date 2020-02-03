#!/usr/bin/python3
"""
a day more for die
"""
import requests
from sys import argv
import json
if __name__ == "__main__":
    theNumId = argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(theNumId))
    showJson = r.json()
    theUserName = showJson.get('username')
    r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                      .format(theNumId))
    showJson2 = r2.json()
    listToJson = []
    theNumId = int(theNumId)
    for js in showJson2:
        dictToJson = {}
        theUserId = js.get('userId')
        completedTF = js.get('completed')
        theTitle = js.get('title')
        dictToJson["username"] = theUserName
        dictToJson["task"] = theTitle
        dictToJson["completed"] = completedTF
        listToJson.append(dictToJson)
    dict_2_Json = {theNumId: listToJson}
    with open('{}.json'.format(theNumId), "w", encoding="utf-8") as j:
        json.dump(dict_2_Json, j)
