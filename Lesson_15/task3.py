"""
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise,
return the result.
"""
from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def arg_rules_dec(func):
        @wraps(func)
        def wrap(name):
            err = []
            if not isinstance(name, type_):
                err.append(f'{name} is not {type_}')
            if len(name) > max_length:
                err.append(f'{name} > {max_length}')
            err.extend(f'not found {i}' for i in contains if i not in name)
            if len(err) == 0:
                return func(name)
            else:
                print(err)
                return False
        return wrap
    return arg_rules_dec


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
    

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

