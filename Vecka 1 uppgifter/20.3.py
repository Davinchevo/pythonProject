def is_palindrome(text):
    first = len(text) - 1
    end = 0
    while first > end:
        if text[first] != text[end]:
            return False
        first -= 1
        end += 1
    return True
    
print(is_palindrome("racecar"))
print(is_palindrome("hello"))