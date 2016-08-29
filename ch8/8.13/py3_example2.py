#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to define various kinds of data structures, but want to enforce
constraints on the values that are allowed to be assigned to certain attributes.
"""


"""
DISCUSSION
"""


# Base class. Uses a descriptor to set a value.
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Decorator for applying type checking
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    super_set = cls.__set__

    def __set__(self, instance, value):
        if isinstance(value, expected_type):
            super_set(self, instance, value)
        else:
            raise TypeError('Expected ' + str(expected_type) + '.')

    cls.__set__ = __set__
    return cls


# Decorator for unsigned values
def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0.')
        else:
            super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Decorator for allowing sized values
def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('Missing size option')
        else:
            super_init(self, name, **opts)

    cls.__init__ = __init__
    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('Size must be < ' + str(self.size) + '.')
        else:
            super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Specialized descriptor
@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass
