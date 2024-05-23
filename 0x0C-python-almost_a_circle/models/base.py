#!/usr/bin/python3

"""wdfbqfgdfhgsdrfgvdsfgV"""
import json


class Base:
    """Wrthgwdgshfvrsdhgfdghfbv"""

    __nb_objects = 0

    def __init__(self, id=None):
        """dfgsdfhgvsdfhgvdtfhgv"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """wdgsvdtjtujtvdthfhfgjvtdfv"""
        if list_dictionaries == None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """utfyufufufyugygyutctyfgiyhiugut"""
        if json_string == None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """wetfgwdfgbdgfb dsgfhbdfxgvdf"""
        dicts = []
        if list_objs is not None:
            for obs in list_objs:
                dicts.append(obs.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """wegvwngvls env rtnhgsvlndgfbjnv """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            obj = Rectangle(1, 1)
        elif cls == Square:
            obj = Square(1)
        else:
            new = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ertgennnfgnhewnfgbwngnto"""
        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        else:
            with open(filename, 'r') as file:
                return [cls.create(**d) for d in cls.from_json_string(file.read())]
