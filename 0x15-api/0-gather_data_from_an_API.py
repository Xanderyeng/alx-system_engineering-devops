#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
"""

import json
import requests
import sys

if __name__ == "__main__":
    argv = sys.argv
    id = argv[1]
    titles = []
    task_comp = 0
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    user_r = requests.get(user_url).json()
    user_name = user_r.get('name')
    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    tasks_r = requests.get(task_url).json()
    tasks = len(tasks_r)
    for task in tasks_r:
        if (task.get('completed') is True):
            task_comp += 1
            titles.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, task_comp, tasks))
    for title in titles:
        print('\t {}'.format(title))
