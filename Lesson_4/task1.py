"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string
length is less than 2, return instead of the empty string.
"""
sample_string = ['helloworld', 'my', 'x']

for s in sample_string:
    if len(s) < 2:
        s = "Empty String"
    else:
        s = s[0:2] + s[-2:]
    print(s)

