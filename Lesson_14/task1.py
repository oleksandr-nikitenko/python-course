"""
Write a Python program to detect the number of local variables declared in a function.
"""


def foo():
    i_str = ''
    i_int = 12
    i_list = [0, 1, 2]
    return True


def count_func(func):
    return func.__code__.co_nlocals


print(count_func(foo))  # 3
