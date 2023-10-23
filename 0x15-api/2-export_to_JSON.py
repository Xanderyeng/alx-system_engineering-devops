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
    list_tasks = []
    for task in tasks_r:
        task_status = task.get('completed')
        title = task.get('title')
        task_dict = {'task': title, 'completed': task_status,
                     'username': user_name}
        list_tasks.append(task_dict)
        dict_final = {id: list_tasks}
    with open('{}.json'.format(id), 'w') as file:
        json.dump(dict_final, file)
