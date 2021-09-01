"""
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""
from random import randrange

list1, list2 = [], []
while True:
    list1.append(randrange(0, 10))
    list2.append(randrange(0, 10))
    if len(list1) == 10 and len(list2) == 10:
        break
        
list3 = list(set(list1) & set(list2))
print(f'list 1: {list1}', f'list 2: { list2}', sep='\n')
print(f'list 3: {list3}')
    

