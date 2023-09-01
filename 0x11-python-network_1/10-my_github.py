#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import requests
from sys import argv
try:
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
except:
    print("None")
