#!/usr/bin/python3
"""Base Model"""
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """new base model"""

    def __init__(self):
        """new intance"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string rep"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current datatime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Dictionary"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
