"""
The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within
Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
"""
import sys

try:
    from phonebook_methods import phone_number_validator
    print('I know this module', phone_number_validator('test'))
except ModuleNotFoundError:
    sys.path.append('../Lesson_10/task2')  # Added new path
    from phonebook_methods import phone_number_validator
    print('Great', phone_number_validator('test'))

sys.path.pop()  # Deleted path

try:
    from phonebook_methods import get_json_object
except ModuleNotFoundError:
    print('Oops')
    