#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """makes a class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value
