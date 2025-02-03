def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("racecar"))

#text[start:stop:step]
#text[::-1] will reverse the text

#[::-1] means:

#start: (empty) → Normally, this means start at index 0,
#BUT because we have a negative step, Python instead starts at the last index (end of the string).
#:stop (empty) → Normally, this means stop at the end,
#BUT because we are going backward, it stops at the beginning (index 0).
#:step (-1) → Move backward one step at a time.

#Why Does Python Start at the End?
#Python Adapts to the Step Direction
#When we write text[start:stop:step], Python looks at the step first:

#If step is positive (1, 2, 3, ...), Python starts at index 0 and moves right.
#If step is negative (-1, -2, -3, ...), Python starts at the last index and moves left.
#So, [::-1] automatically starts at the end because of the -1 step.