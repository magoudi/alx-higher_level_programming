#!/usr/bin/python

"""Adrgnjanskgnvlajlbnsg"""
from urllib import request

resp = request.urlopen("https://alx-intranet.hbtn.io/status")
data = resp.read()

print(f"\t- type: {type(data)}$")
print(f"\t- content: {data}$")
print(f"\t- utf8 content: {data.decode("UTF-8")}$")
