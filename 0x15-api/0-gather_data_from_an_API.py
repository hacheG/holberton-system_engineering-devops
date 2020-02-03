#!/usr/bin/python3
"""a day more for die"""

import requests
from sys import argv

if __name__ == "__main__":

    numTaskCompĺete = 0
    theNumId = argv[1]

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(theNumId))
    showJson = r.json()
    oneId = showJson.get('name')

    r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                      .format(theNumId))
    showJson2 = r2.json()
    numberJson = len(showJson2)

    for json in showJson2:
        if json.get('completed') is True:
            numTaskCompĺete = numTaskCompĺete + 1

    r3 = requests.get('https://jsonplaceholder.typicode.com/posts/{}'
                      .format(theNumId))
    comment = r3.json()
    bodyComment = comment.get('body')

    print ('Employee {} is done with task {}/{}:\n{} '
           .format(oneId, numTaskCompĺete, numberJson, bodyComment))
