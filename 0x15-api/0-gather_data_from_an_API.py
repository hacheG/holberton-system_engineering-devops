#!/usr/bin/python3
"""
a day more for die
"""

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


def print_completed_tasks(data):
    total = len(data.get('tasks'))
    completed_tasks = [t for t in data.get('tasks') if t.get('completed')]
    completed = len(completed_tasks)
    print('Employee {} is done with tasks({}/{}):'
          .format(data.get('employee').get('name'), completed, total))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    data = get_employee_tasks(argv[1])
    print_completed_tasks(data)
