"""
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the
second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""
from math import prod


def make_operation(operator: str, *args: int) -> int:
    result = 0
    if operator in ['+', '-', '*'] and all(isinstance(x, int) for x in args):
        if operator == '+':
            result = sum(args)
        elif operator == '*':
            result = prod(args)
        elif operator == '-':
            return args[0] - sum(args[1:])
    else:
        print('Unknown operator or arg is not int.')
        result = 0
    return result
