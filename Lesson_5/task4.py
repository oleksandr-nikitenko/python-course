"""
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then
responds with a message accordingly.
"""
asks = '2 * 2 = ?', '5 * 6 = ?', ' 7 * 8 = ?'
for ask in asks:
    num = int(input(ask+'\n'))
    print(True if num == 2*2 else False)
    
