#!/usr/bin/python3
"""The class that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the hbnb project"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timefrm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timefrm)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['update_at'] = self.update_at.isoformat()
        return obj_dict
