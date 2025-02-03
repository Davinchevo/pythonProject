def isItAVowel(char):
    vowels = "aeiouy"
    if char in vowels:
        return True
    else:
        return False

input_char = input("Enter a character: ")
print(isItAVowel(input_char))