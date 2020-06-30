#!/usr/bin/python3
import uuid
from datetime import datetime, timezone
import models


class BaseModel:

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
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.__class__.save(self)

    def to_dict(self):
        dict2 = dict(self.__dict__)
        dict2["__class__"] = self.__class__.__name__
        dict2["updated_at"] = self.updated_at.isoformat()
        dict2["created_at"] = self.created_at.isoformat()
        return dict2
