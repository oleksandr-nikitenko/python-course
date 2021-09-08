from .module2 import test_function_mod2


def test_function_mod1():
    return f' "{test_function_mod1.__name__}" from "{__file__.split("/")[-1]}"'


if __name__ == '__main__':
    None