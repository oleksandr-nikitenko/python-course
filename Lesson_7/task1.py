"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
the number of occurrences as values.
"""


def word_counter(s: str) -> dict:
    result = dict()
    for i in s.split(' '):
        if result.get(i) is None:
            result[i] = 1
        else:
            result[i] += 1
    return result


print(word_counter('Make a program that has some sentence a string on input and returns a dict containing '
                   'all unique words as keys and the number of occurrences as values. '.lower()))
