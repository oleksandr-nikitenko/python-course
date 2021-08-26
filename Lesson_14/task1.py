"""
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
"""
from functools import wraps


def logger(func):
    @wraps(func)
    def wrap(*args):
        print(f'{func.__name__} called with {", ".join(str(a) for a in args)} ')
    return wrap
    

@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(1, 2)
square_all(1, 2, 3, 4, 5)
