"""
Write a program that reads in a sequence of characters and prints them in reverse order, using your
implementation of Stack.
"""
from stack import Stack


def reverse_order(characters: str) -> Stack:
    stck = Stack()
    for char in characters:
        stck.push(char)
    return stck


if __name__ == "__main__":
    print(reverse_order('sequence of characters'))
