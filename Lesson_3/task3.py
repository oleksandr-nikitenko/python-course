stored_name = 'Oleksandr'
input_name = input('Enter your name:\n').strip()

if stored_name.lower() == input_name.lower():
    print('Names are equal.')
else:
    print('Names are not equal.')
    