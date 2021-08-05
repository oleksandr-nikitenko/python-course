
asks = '2 * 2 = ?', '5 * 6 = ?', ' 7 * 8 = ?'
for ask in asks:
    num = int(input(ask+'\n'))
    print(True if num == 2*2 else False)
    
