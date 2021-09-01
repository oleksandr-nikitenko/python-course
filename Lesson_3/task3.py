"""
Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""
a = 17
b = 5

# Addition
print(a + b)

# Subtraction
print(a - b)

# Division
try:
    print(a / b)
except ZeroDivisionError:
    print('Division by zero!')

# Multiplication
print(a * b)

# Exponent
print(a ** b)

# Modulus
try:
    print(a // b)
except ZeroDivisionError:
    print('Division by zero!')

# Floor division
try:
    print(a % b)
except ZeroDivisionError:
    print('Division by zero!')





