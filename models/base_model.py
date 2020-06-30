#!/usr/bin/python3
"""BaseModel Class File"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """init func
        args:
        """
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
        """str func
        return str
        """

        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save func
        args:
        self
        """

        self.updated_at = datetime.now()
        models.storage.__class__.save(self)

    def to_dict(self):
        """to_dict func
        args:
        self
        """
        dict2 = dict(self.__dict__)
        dict2["__class__"] = self.__class__.__name__
        dict2["updated_at"] = self.updated_at.isoformat()
        dict2["created_at"] = self.created_at.isoformat()
        return dict2
