#!/usr/bin/python3
"""takes in a letter and sends a POST request """
import requests
import sys


if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    try:
        resp = requests.post(url, data={'q': q}).json()
    except:
        print("Not a valid JSON")
    else:
        if resp:
            print("[{}] {}".format(resp['id'], resp['name']))
        else:
            print("No result")
