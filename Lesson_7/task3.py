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



