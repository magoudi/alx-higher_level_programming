#!/usr/bin/python3

"""Adrgnjanskgnvlajlbnsg"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
