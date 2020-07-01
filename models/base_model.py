#!/usr/bin/python3
"""BaseModel file Doc"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        models.storage.__class__.save(self)

    def to_dict(self):
        """to dict method"""
        dictnew = dict(self.__dict__)
        dictnew["__class__"] = self.__class__.__name__
        dictnew["updated_at"] = self.updated_at.isoformat()
        dictnew["created_at"] = self.created_at.isoformat()
        return dictnew
