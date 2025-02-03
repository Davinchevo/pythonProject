def is_palindrome(text):
    text_list = list(text)
    text_list.reverse()
    txt = ''.join(text_list)
    print(txt)
    print(text)
    if txt == text:
        return True
    else:
        return False
    
print(is_palindrome("racecar"))
