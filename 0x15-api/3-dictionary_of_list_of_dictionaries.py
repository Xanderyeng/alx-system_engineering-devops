#!/usr/bin/python3
"""
script to export data in the CSV format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    titles = []
    task_comp = 0
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    user_r = requests.get(user_url).json()
    dict_final = {}
    for id in range(1, len(user_r) + 1):
        dict_final[id] = []
        user_n = requests.get('{}/{}'.format(user_url, id))
        user_name = user_n.json().get('username')
        r = requests.get('{}{}/todos'.format(user_url, id))
        tasks_r = r.json()
        list_tasks = []
        for task in tasks_r:
            task_status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict = {'task': title, 'completed': task_status,
                         'username': user_name}
            list_tasks.append(task_dict)
        dict_final[id] = list_tasks
    with open('todo_all_employees.json'.format(id), 'w') as file:
        json.dump(dict_final, file)
