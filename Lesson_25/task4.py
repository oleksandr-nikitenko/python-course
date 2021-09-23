def reverse(input_str: str) -> str:
    return input_str if len(input_str) == 0 else input_str[-1] + reverse(input_str[0:-1])
        

print(reverse('hello')) # olleh 
print(reverse('o'))     # o
