def is_palindrome(inStr):
    front = 0
    end = len(inStr) - 1

    while inStr[front].lower() == inStr[end].lower() and front < end:
        front += 1
        end -= 1

    if front < end:
        return False
    else:
        return True