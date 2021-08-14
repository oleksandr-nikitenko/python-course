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
