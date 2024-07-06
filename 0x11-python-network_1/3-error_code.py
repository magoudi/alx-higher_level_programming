#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    request = request.Request(url)
    try:
        with request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
