#!/usr/bin/python3

"""Adrgnjanskgnvlajlbnsg"""
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    data = resp.read()
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: " + data.decode("UTF-8"))
