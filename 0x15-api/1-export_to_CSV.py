#!/usr/bin/python3
"""
script to export data in the CSV format.
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
    user_name = user_r.get('username')
    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    tasks_r = requests.get(task_url).json()
    with open('{}.csv'.format(id), 'w') as file:
        for task in tasks_r:
            task_status = task.get('completed')
            title = task.get('title')
            file.write('"{}","{}","{}","{}"\n'
                       .format(id, user_name, task_status, title))
