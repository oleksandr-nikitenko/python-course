"""
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a
valid email string.
"""
import re


class Validator:
    _regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    def __init__(self, email: str) -> None:
        if Validator.validate(email):
            self.email = email
        else:
            raise ValueError(f'E-mail: {email} - is not valid.')
    
    @classmethod
    def validate(cls, email: str) -> bool:
        return True if re.fullmatch(cls._regex, email) else False