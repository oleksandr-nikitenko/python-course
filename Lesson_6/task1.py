"""
Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""
from random import randrange

list_nums = []
max_num = 0
while True:
    random_num = randrange(0, 999)
    list_nums.append(random_num)
    if max_num < random_num: max_num = random_num  # 2 without use max()
    if len(list_nums) == 10:
        print(max_num)          # 2 without use max()
        break
print(max(list_nums))
print(list_nums)

    
    

