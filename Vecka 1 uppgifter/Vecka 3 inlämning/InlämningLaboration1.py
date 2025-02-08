


hangman = input("Enter a word: ")
list_of_characters = list(hangman)

# Create a dictionary with "*" as the key and the value as a string of asterisks of the same length as the word
dict_of_stars = {"*" * len(hangman) }

print(dict_of_stars)
