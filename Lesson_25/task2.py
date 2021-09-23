
def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


print(is_palindrome('mom'))     # True
print(is_palindrome('sassas'))  # True
print(is_palindrome('o'))       # True

