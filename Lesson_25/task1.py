from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp < 0:
        raise ValueError('This function works only with exp > 0.')
    return x * to_power(x, exp - 1) if exp != 0 else 1


print(to_power(2, 3) == 8)          # True
print(to_power(3.5, 2) == 12.25)    # True
print(to_power(2, -1))              # ValueError: This function works only with exp > 0.
