"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
input function were not numbers, and if value b was zero (cannot divide by zero).
"""


def func(a: int, b: int) -> float:
    try:
        return int(a)**2 / int(b)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
  
        
result = func(input('a: '), input('b: '))
print(result)