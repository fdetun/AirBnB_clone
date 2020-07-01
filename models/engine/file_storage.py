#!/usr/bin/python3
"""
"""
import json

from models.base_model import BaseModel
from models.user import User


Cls = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects['.'.join((
            obj.__class__.__name__, str(obj.id)))] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        __objects must be updated
        """
        Tmp_dict = {}
        for Key, Val in FileStorage.__objects.items():
            Tmp_dict[Key] = Val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(Tmp_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects.
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp = json.load(f)
                for Key, Value in tmp.items():
                    FileStorage.__objects[str(Key)] = Cls[Key.split(".")[
                        0]](**Value)
        except Exception as e:
            pass
