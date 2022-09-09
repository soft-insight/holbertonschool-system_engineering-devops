#!/usr/bin/python3
""" export data in the JSON format
"""

import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    urlApi = 'https://jsonplaceholder.typicode.com'
    user = requests.get(urlApi + f'/users/{user_id}').json()

    user_tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                              params={'userId': user_id}).json()

    print(user)
