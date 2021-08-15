
def func(a: int, b: int) -> float:
    try:
        return int(a)**2 / int(b)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
  
        
result = func(input('a: '), input('b: '))
print(result)