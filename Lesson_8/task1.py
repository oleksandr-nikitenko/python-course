def oops():
    raise IndexError('Oops')

    
def another_function():
    try:
        oops()
    except Exception as e:
        print(e.__str__())
        

