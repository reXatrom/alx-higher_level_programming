#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. using the
package requests and sys.
"""
import sys
import requests


if __name__ == "__main__":
    element = "" if len(sys.argv) == 1 else sys.argv[1]
    content = {"q": element}

    req = requests.post("http://0.0.0.0:5000/search_user", data=content)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
