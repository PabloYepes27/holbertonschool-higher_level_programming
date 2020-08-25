#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    req = requests.post(url, data=values)
    if (len(req.json()) is not 0 and req.json.get(
            'id') and req.json.get('name')):
        try:
            print('[{}] {}'.format(req.json()['id'], req.json()['name']))
        except:
            print("Not a valid JSON")
    else:
        print("No result")
