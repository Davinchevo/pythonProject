
character = input("Enter a character: ")

vowel = "aeiouy"

if vowel.__contains__(character):
    print(f"{character} is a vowel")

else:
    print(f"{character} is a consonant")
