#!/usr/bin/python3
"""pyhton interpreter"""
import json
from os import path
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.user import User


class FileStorage():
    """class fileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """
        This function creates a new object of class BaseModel
        and adds it to the dictionary __objects.
        :param obj: the object to be stored
        """

        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_objec = {}

        for key, value in self.__objects.items():
            dict_objec[key] = value.to_dict()
        with open(self.__file_path, mode='w') as file:
            file.write(json.dumps(dict_objec))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as fileJr:
                loaded_dictionary = json.loads(fileJr.read())
            for values in loaded_dictionary.values():
                execsClass = values["__class__"]
                self.new(eval(execsClass)(**values))
