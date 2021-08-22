#!/usr/bin/python3
"""script that takes in a URL and an email, send a POST request and display"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    mail = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('ascii')

    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
