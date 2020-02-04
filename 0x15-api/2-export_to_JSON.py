#!/usr/bin/python3
"""
a day more for die
"""

import json
import requests
from sys import argv


def get_employee_tasks(user_id):
    '''Retrieves employees and tasks'''
    url = 'https://jsonplaceholder.typicode.com/'
    user_req = url + 'users/{}'.format(user_id)
    employee = requests.get(user_req).json()
    task_req = url + 'todos?userId={}'.format(employee.get('id'))
    tasks = requests.get(task_req).json()
    return {"employee": employee, "tasks": tasks}


def export_to_json(data):
    '''Exports dict to json'''
    _id = data.get('employee').get('id')
    _array = []
    for task in data.get('tasks'):
        d = {}
        d['task'] = task.get('title')
        d['completed'] = task.get('completed')
        d['username'] = data.get('employee').get('username')
        _array.append(d)
    _dict = {_id: _array}
    with open('{}.json'.format(_id), 'w') as json_file:
        json.dump(_dict, json_file)


if __name__ == '__main__':
    data = get_employee_tasks(argv[1])
    export_to_json(data)
