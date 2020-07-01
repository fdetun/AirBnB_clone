#!/usr/bin/python3
"""
file storage File
"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """File Storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all func"""
        return FileStorage.__objects

    def new(self, obj):
        """all func"""
        a = obj.__class__.__name__
        b = obj.id
        FileStorage.__objects[str(a) + "." + str(b)] = obj

    def save(self):
        """all func"""
        tmp = {}
        for key, value in FileStorage.__objects.items():
            tmp[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(tmp, file)

    def reload(self):
        """all func"""
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
            for k, i in data.items():
                FileStorage.__objects[str(k)] = BaseModel(**i)
        except:
            pass
