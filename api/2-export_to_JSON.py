#!/usr/bin/python3
"""Script that exports employee TODO data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    username = user.get("username")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    data = {str(employee_id): tasks}

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
