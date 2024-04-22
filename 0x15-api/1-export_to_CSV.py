#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [argv[1], username, to.get("completed"), to.get("title")])
            for to in todos]
