#!/usr/bin/python3
"""a day more for die"""

import json
import requests
from sys import argv


def get_all_tasks():
    ''' Returns dict of employee and all tasks '''
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    tasks = requests.get(url + 'todos').json()
    _dict = {}
    for u in users:
        _list = []
        for task in tasks:
            if u.get('id') == task.get('userId'):
                d = {}
                d['task'] = task.get('title')
                d['completed'] = task.get('completed')
                d['username'] = u.get('username')
                _list.append(d)
        _dict[u.get('id')] = _list
    return _dict


if __name__ == '__main__':
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(get_all_tasks(), json_file)
