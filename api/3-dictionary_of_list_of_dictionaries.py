#!/usr/bin/python3
"""Script that exports all employees' TODO data to a JSON dictionary."""
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
            if task.get("userId") == user_id
        ]
        all_data[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
