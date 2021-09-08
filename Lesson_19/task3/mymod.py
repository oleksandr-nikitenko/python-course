"""
Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, for additional info about it
follow the link: https://www.geeksforgeeks.org/wc-command-linux-examples/ or in case you have macOS or Linux -
just call manual for this utility via command: `man wc`).
"""

from os import path
from sys import argv


def count_lines(file) -> int:
    return len(file.readlines())


def count_words(file) -> int:
    return len(file.read().replace('\n', ' ').split(' '))


def count_chars(file) -> int:
    return len(file.read())
    
    
def test(file_path):
    if path.isfile(file_path) and isinstance(file_path, str):
        file = open(file_path, 'r')
        lines = count_lines(file)
        file.seek(0)
        words = count_words(file)
        file.seek(0)
        chars = count_chars(file)
        file.close()
        print(lines, words, chars, file_path.split('/')[-1], sep='\t')
    else:
        print(f'"{file_path}" not string or "{file_path}" not found.')
        

if __name__ == '__main__':
    if len(argv) > 1:
        for a in argv:
            test(a)

        