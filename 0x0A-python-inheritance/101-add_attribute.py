#!/usr/bin/python3
"""adds a new attribute to an object
if possible
"""


def add_attribute(obj, attribute, value):
    """adds a new attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can not add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can not add new attribute")
    else:
        setattr(obj, attribute, value)
