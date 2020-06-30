#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        a = obj.__class__.__name__
        b = obj.id
        FileStorage.__objects[str(a) + "." + str(b)] = obj

    def save(self):
        tmp = {}
        for key, value in FileStorage.__objects.items():
            tmp[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(tmp, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
            for k, i in data.items():
                FileStorage.__objects[str(k)] = BaseModel(**i)
        except:
            pass