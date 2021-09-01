"""
Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but
not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration
"""
list0, list1 = [], []

i = 1
while i <= 100:
    list0.append(i)
    i += 1
j = 0
while j < len(list0):
    if list0[j] % 7 == 0 and list0[j] % 5 != 0:
        list1.append(list0[j])
    j += 1
print(list1)

