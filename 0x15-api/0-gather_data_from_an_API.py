#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(completed), len(todos)))
    [print("\t {}".format(com)) for com in completed]
