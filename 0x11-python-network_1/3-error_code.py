#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). using urllib and sys as the only
packages.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as reply:
            print(reply.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
