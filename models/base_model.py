#!/usr/bin/python3
"""
Base Model module
"""
import models
import uuid
from datetime import datetime
date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        creates a BaseModel object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"], date)
            self.updated_at = datetime.strptime(kwargs["updated_at"], date)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        string representation of the BaseModel class
        """
        return ("[{}] ({}) {})".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        """
        Updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['created_at'] = self.created_at.isoformat()
        return dictionary
