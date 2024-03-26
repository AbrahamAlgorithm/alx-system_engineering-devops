#!/usr/bin/python3
"""Importing Api from an url"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data['name']
        total_tasks = len(todo_data)
        completed_tasks = [task for task in todo_data if task['completed']]

        print(
                "Employee {} is done with tasks({}/{})".format(
                    employee_name, len(completed_tasks), total_tasks
                    ) + ":"
                )

        for task in completed_tasks:
            print("\t{}".format(task["title"]))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
