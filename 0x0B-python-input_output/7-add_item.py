#!/usr/bin/python3

"""wgjbwgsgsdgvsfgvdfsgdfgv dfgv"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    mylist = load_from_json_file("add_item.json")
except Exception:
    mylist = list()
for i in range(1, len(argv)):
    mylist.append(argv[i])
save_to_json_file(mylist, "add_item.json")
