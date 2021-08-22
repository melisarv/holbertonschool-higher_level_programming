#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":

    user = requests.get("https://api.github.com/user",
                        auth=(sys.argv[1], sys.argv[2]))
    try:
        resp = user.json()
    except:
        print("Not a valid JSON")
    else:
        print(resp.get('id'))
