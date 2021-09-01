"""
Write a class TypeDecorators which has several methods for converting results of functions to a specified type
(if it's possible): to_int, to_str, to_bool, to_float
"""
from functools import wraps


class TypeDecorators:
    
    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrap(string):
            return str(string)
        return wrap
    
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrap(string):
            try:
                return int(string)
            except TypeError as e:
                return e
        return wrap

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrap(string):
            try:
                return bool(string)
            except TypeError as e:
                return e
        return wrap

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrap(string):
            try:
                return float(string)
            except TypeError as e:
                return e
            except ValueError as e:
                return e
        return wrap


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True