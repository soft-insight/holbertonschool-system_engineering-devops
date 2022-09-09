#!/usr/bin/python3
""" Export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    urlApi = 'https://jsonplaceholder.typicode.com'
    user = requests.get(urlApi + f'/users/{user_id}').json()

    user_tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                              params={'userId': user_id}).json()

    filename = f'{user_id}.csv'

    with open(filename, 'w', newline='') as f:
        data2csv = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in user_tasks:
            data2csv.writerow([int(user_id),
                               user.get('username'),
                               i.get('completed'),
                               i.get('title')])
