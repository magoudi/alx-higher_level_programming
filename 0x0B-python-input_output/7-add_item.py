#!/usr/bin/python3

"""wgjbwgsgsdgvsfgvdfsgdfgv dfgv"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


mylist = load_from_json_file("add_item.json")
for i in argv:
    mylist.append(i)
save_to_json_file("add_item.json", mylist)
