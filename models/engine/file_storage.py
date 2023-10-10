#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file
to instances"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        classname = obj.__class__.__name__
        key = "{}.{}".format(classname, obj.id)
        slef.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    loaded_objects = json.load(file)
                    for key, obj_dict in loaded_objects.items():
                        class_name, obj_id = key.split('.')
                        class_obj = models[class_name]
                        self.__objects[key] = class_obj(**obj_dict)
                except json.JSONDecodeError:
                    pass
