#!/usr/bin/python3

"""jnviwnfvingtigfnisrndgdng"""
toJson = __import__("3-to_json_string").to_json_string
write_file = __import__('1-write_file').write_file


def save_to_json_file(my_obj, filename):
    """rtgnvjndfgsisengdrofcmosdfgd"""
    write_file(filename, toJson(my_obj))
