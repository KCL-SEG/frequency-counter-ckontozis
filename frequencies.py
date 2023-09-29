"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for item in items:
        if not isinstance(item, str):
            key = str(item)
        else:
            key = item

        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1
    return frequencies
