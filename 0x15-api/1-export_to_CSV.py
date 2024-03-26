#!/usr/bin/python3
"""import api from a url"""
import requests
import sys

if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
        url = "https://jsonplaceholder.typicode.com"
        res = requests.get('{}/users/{}'.format(url, id)).json()
        res_todo = requests.get("{}/todos".format(url),
                                params={"userId": id}).json()
        name = res.get("username")
        with open('{}.csv'.format(id), 'w') as apidata:
            for todo in res_todo:
                apidata.write(
                    '"{}","{}","{}","{}"\n'.format(id, name,
                                                   todo.get('completed'),
                                                   todo.get('title'))
                )
    except ValueError:
        pass
