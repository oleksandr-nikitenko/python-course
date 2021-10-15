"""
Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly
brackets are "balanced."
"""

from queue import Queue


def is_balanced(characters: str):
    q = Queue()
    for char in characters:
        q.enqueue(char)
    start, end = ['[', '{', '(', '<'], [']', '}', ')', '>']
    count_chars = {'[': 0, '{': 0, '(': 0, '<': 0}
    for i in reversed(q.items):
        if i in start:
            count_chars[i] += 1
        elif i in end:
            if count_chars[start[end.index(i)]] >= 1:
                count_chars[start[end.index(i)]] -= 1
        else:
            continue
    result = ''
    for i in count_chars:
        if i in characters:
            result += f'"{i}" -> {"Balanced" if count_chars[i] == 0 else "Unbalanced"} \n'
    return result
    
    
if __name__ == "__main__":
    with open('task1.py') as f:
        file1 = f.read()
    with open('task2.py') as f:
        file2 = f.read()
    print('task1.py', is_balanced(file1), sep='\n')
    print('task2.py', is_balanced(file2), sep='\n')




