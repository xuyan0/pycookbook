#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

When creating instances of a class, you want to return a cached reference to a
previous instance created with the same arguments (if any).
"""


"""
DISCUSSION
"""

import weakref


class CachedSpamManager(object):

    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name in self._cache:
            s = self._cache[name]
        else:
            s = Spam(name)
            self._cache[name] = s
        return s

    def clear(self):
        self._cache.clear()


class Spam(object):

    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam.manager.get_spam(name)


if __name__ == '__main__':
    a = Spam('foo')
    b = Spam('foo')
    print(a is b)
