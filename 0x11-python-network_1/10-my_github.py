#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id. using packages like requests and sys
only.
"""
from requests import get
from sys import argv

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=(username, password))
    json = response.json()

    print(json.get('id'))
