def check_guess(guess_char):
    lifes = 6
    while lifes > 0:
        for i in range(len(list_of_characters)):
            if guess_char == list_of_characters[i]:
                dict_of_stars[i] = guess_char
            else:
                lifes -= 1
                print("Wrong guess, you have", lifes, "lifes left")


hangman = input("Enter a word: ")
list_of_characters = list(hangman)

dict_of_stars = {"*" * len(hangman) }

print(dict_of_stars)
