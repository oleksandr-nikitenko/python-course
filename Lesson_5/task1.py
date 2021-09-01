"""
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""
from random import randint

print('Enter \'999\' to EXIT.')
while True:
    number = randint(1, 10)
    try:
        input_number = int(input('Enter a number from 1 to 10:\n'))
    except ValueError:
        print('ERROR: You entered incorrect data!')
        continue
    # Exit
    if input_number == 999:
        print('GAME OVER.')
        break
    
    if input_number not in range(1, 11):
        print('WARNING: The number must be in the range from 1 to 10.')
        continue
    else:
        if number == input_number:
            print(f'You answered correctly! ({number})!\n GAME OVER.')
            break
        else:
            print(f'You answered wrong! ({number})')
            continue
