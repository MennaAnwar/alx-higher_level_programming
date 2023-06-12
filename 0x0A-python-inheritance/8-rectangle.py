#!/usr/bin/python3
"""basegeometryclass"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""class rectangle"""

class Rectangle(BaseGeometry):
    """creates rectangle class"""
    
    def __init__(self, width, height):
        """initializes rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
