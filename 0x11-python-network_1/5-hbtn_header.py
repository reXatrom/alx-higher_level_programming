#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header. using the sys and
requests packages."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
