#!/usr/bin/python3
"""import api from a url"""
import json
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
        user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": name
                    },
                    res_todo
                ))
        with open('{}.json'.format(id), 'w') as apidata:
            data = {
                "{}".format(id): user_data
            }
            json.dump(data, apidata)
    except ValueError:
        pass
