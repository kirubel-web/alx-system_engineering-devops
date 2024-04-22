#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
            "task": to.get("title"),
            "completed": to.get("completed"),
            "username": username
            } for to in todos
            ]}, jsonfile)
