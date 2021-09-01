"""
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def ext_func():
    print(f'Hello. I am external function "{ext_func.__name__}"')
    
    def int_func():
        return f'Hello. I am internal function "{int_func.__name__}"'
    return int_func


print(ext_func()())
