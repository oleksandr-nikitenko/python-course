"""
Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True.
"""
stored_name = 'Anton'
input_name = input('Enter your name:\n').strip()

if stored_name.lower() == input_name.lower():
    print('Names are equal.')
else:
    print('Names are not equal.')
    