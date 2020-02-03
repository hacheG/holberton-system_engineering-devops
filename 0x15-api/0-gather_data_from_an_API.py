#!/usr/bin/python3
"""
a day more for die
"""

import requests
from sys import argv

if __name__ == "__main__":

    numTaskCompĺete = 0
    totalUserId2 = 0
    totalTrue = 0
    theNumId = argv[1]

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(theNumId))
    showJson = r.json()
    theName = showJson.get('name')

    r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                      .format(theNumId))
    showJson2 = r2.json()

    theNumId = int(theNumId)
    for q in showJson2:
        if q.get("userId") == theNumId:
            totalUserId2 = totalUserId2 + 1
            theTrue = q.get("completed")
            if theTrue is True:
                totalTrue = totalTrue + 1

    print ('Employee {} is done with tasks {}/{}:'
           .format(theName, totalTrue, totalUserId2))
    for q in showJson2:
        if q.get("userId") == theNumId:
            theTrue = q.get("completed")
            if theTrue is True:
                print (q.get("title"))
