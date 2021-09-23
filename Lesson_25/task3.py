def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError('This function works only with positive integers')
    return a if n == 0 else a + mult(a, n-1)
       


print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
print(mult(2, -4) == 0)
