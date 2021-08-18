"""
Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its
functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality
for saving messages to file
"""
from datetime import datetime as dt


class CustomException(Exception):
    __path_log = 'logs.txt'
    
    def __init__(self, msg):
        self.__add_to_log(msg, dt.now().strftime("%H:%M:%S %d.%m.%Y"))
    
    def __add_to_log(self, msg, datetime):
        with open(CustomException.__path_log, 'a') as file:
            file.write(f'[{datetime}] {msg} \n')
    
    
custom_exception = CustomException('Oops, something went wrong!')
raise custom_exception
    