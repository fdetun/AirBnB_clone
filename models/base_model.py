#!/usr/bin/python3
import uuid
from datetime import datetime, timezone

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.save()
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dict2 = dict(self.__dict__)
        dict2["__class__"] = self.__class__.__name__
        dict2["updated_at"] = self.updated_at.isoformat()
        dict2["created_at"] = self.created_at.isoformat()
        return dict2