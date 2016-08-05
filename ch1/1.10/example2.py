#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to eliminate the duplicate values in a sequence, but preserve the order
of the remaining items.
"""


"""
SOLUTION FOR UNHASHABLE ELEMENTS
"""

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 2, 'y': 4}
    ]
    print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe(a, key=lambda d: (d['x']))))
