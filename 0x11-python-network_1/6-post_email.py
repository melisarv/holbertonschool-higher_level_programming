#!/usr/bin/python3
"""takes in a URL and email, sends a POST request to the passed URL"""
import requests
import sys


if __name__ == "__main__":

    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
