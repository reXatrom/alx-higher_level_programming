#!/usr/bin/python3
"""a python script that fetches https://alx-intranet.hbtn.io/status using urlib package
"""
import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as answer:
        element = answer.read()
        print("Body response:")
        print("\t- type: {}".format(type(element)))
        print("\t- content: {}".format(element))
        print("\t- utf8 content: {}".format(element.decode('utf-8')))
