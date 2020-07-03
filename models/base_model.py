#!/usr/bin/python3
"""
base models
"""
import uuid
from datetime import datetime, timezone, timedelta
import models


class BaseModel:
    """
    BaseModel DOC
    """
    def __init__(self, *args, **kwargs):
        """
        abc
        """
        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, To_Date(val))
                elif key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """
            call to the method new(self) on storage
            """
            models.storage.__class__.new(models.storage, self)

    def __str__(self):
        """
        abc
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        """
        abc
        """
        self.updated_at = datetime.now()
        """
        call save(self) method of models.storage
        -->try Using FileStorage.save(storage)
        """
        models.storage.__class__.save(self)

    def to_dict(self):
        """
        abc
        """
        dict2 = dict(self.__dict__)
        dict2["__class__"] = self.__class__.__name__
        dict2["updated_at"] = self.updated_at.isoformat()
        dict2["created_at"] = self.created_at.isoformat()
        return dict2


def To_Date(str_dt):
    """
    Function to transform datetime representation to datetime object
    """
    Splittet_List = str_dt.split(".")
    Part1 = datetime.strptime(Splittet_List[0], "%Y-%m-%dT%H:%M:%S")
    Part2 = int(Splittet_List[1].rstrip("Z"), 10)
    return Part1 + timedelta(microseconds=Part2)
