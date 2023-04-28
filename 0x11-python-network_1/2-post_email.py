#!/usr/bin/python3
"""a python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response. using packages like urllib and sys.
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, info)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
