"""
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”
"""
name = input('Your name: ').strip()
while True:
    try:
        age = int(input('Your age: '))
        if age not in range(1, 100):
            print('ERROR: You entered incorrect data!')
            continue
    except ValueError:
        print('ERROR: You entered incorrect data!')
        continue
    break
    
print(f'Hello {name}, on your next birthday you’ll be {age + 1} years')
