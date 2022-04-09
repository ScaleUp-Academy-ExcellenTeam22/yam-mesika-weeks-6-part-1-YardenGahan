"""
This program overloads the function "filter".
"""


def my_filter(func, values):
    result = []
    for val in values:
        if func(val):
            yield val
