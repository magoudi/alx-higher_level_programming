#!/usr/bin/python3

"""fneidnsgfrusdfnciwdnfinfcs"""


class Student:
    """wegwgwegwedhgvwfagwehth"""

    def __init__(self, first_name, last_name, age):
        """sfdgsdfgwfgwgfvafrg5rgergv"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """wsgrrgveagwfgdbfsdFB"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """hjbjhbjhbjhbhjbhjbhjbjhbjhb"""
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
