#!/usr/bin/python3
"""
Importing API from an URL
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from REST API

    Parameters:
        employee_id (int): The ID of the employee

    Returns:
        None
    """

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

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
