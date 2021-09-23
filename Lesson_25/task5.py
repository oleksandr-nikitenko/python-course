def sum_of_digits(digit_string: str) -> int:
    try:
        int(digit_string)
    except ValueError:
        raise ValueError('Input string must be digit string.') from None
    return int(digit_string[0]) if len(digit_string) == 1 else int(digit_string[0]) + int(sum_of_digits(digit_string[1:])) 

print(sum_of_digits('26'))
print(sum_of_digits('test'))
