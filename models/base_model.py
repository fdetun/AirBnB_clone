#!/usr/bin/python3
""" BaseModel file"""
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class"""
    def __init__(self):
        """ init func"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str func"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ save class"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict function"""
        dict2 = dict(self.__dict__)
        dict2["__class__"] = self.__class__.__name__
        dict2["updated_at"] = self.updated_at.isoformat()
        dict2["created_at"] = self.created_at.isoformat()
        return dict2
