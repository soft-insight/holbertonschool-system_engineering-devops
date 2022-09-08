#!/usr/bin/python3
""" From REST API: "https://jsonplaceholder.typicode.com/"
    returns info about TODO list.
"""
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    urlApi = 'https://jsonplaceholder.typicode.com/users/user_id'
    user = requests.get(urlApi).json()

    user_tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                              params={'userId': user_id}).json()

    num_user_task = len(user_tasks)
    user_name = user.get('name')

    num_task_completed = 0
    for i in range(num_user_task):
        if user_tasks[i]['completed']:
            num_task_completed += 1

    print('Employee {} is done with tasks({}/{}):'.format(
          user_name, num_task_completed, num_user_task))

    num_task_completed = 0
    for i in range(len(user_tasks)):
        if user_tasks[i]['completed']:
            print('\t', user_tasks[i]['title'])
            num_task_completed += 1
