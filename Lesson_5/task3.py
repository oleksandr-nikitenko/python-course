"""
Create a program that reads an input string and then creates and prints 5 random strings from characters of the input
string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
"""
import random
word = list(input('Enter your string: '))

# 1
for i in range(0, 5):
    random.shuffle(word)
    print(''.join(word), end=', ')

print()

# 2
for i in range(0, 5):
    copy_word = word.copy()
    for j in range(0, len(word)):
        print(copy_word.pop(random.randint(0, len(copy_word)-1)), end='')
    print(end=', ')
    