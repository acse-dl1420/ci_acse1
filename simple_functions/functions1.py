from functools import lru_cache
import numpy as np

__all__ = ['my_sum', 'factorial', 'trig_function']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1

def trig_function(iterable):
    return np.sin(iterable)