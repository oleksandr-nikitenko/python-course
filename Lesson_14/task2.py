"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""
from functools import wraps


def stop_word(word: list):
    def stop_word_dec(func):
        @wraps(func)
        def wrap(name):
            result = func(name)
            for w in word:
                result = result.replace(w, '*')
            return result
        return wrap
    return stop_word_dec


@stop_word(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
