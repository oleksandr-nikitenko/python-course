"""
Make a program that checks if a string is in the right format for a phone number. The program should check that the
string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the
outcome of the string evaluation.
"""
phone_number = '0639999999'

if len(phone_number) == 0 and phone_number.isdigit():
    print('Phone number is valid!')
else:
    print('Phone number is not valid!')
