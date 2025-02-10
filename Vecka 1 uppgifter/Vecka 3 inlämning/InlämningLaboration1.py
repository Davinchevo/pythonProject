def hangman():
    lifes = 6
    incorrect_guesses = ""
    while lifes > 0:
        input_char = input("Enter a character: ")
        if len(input_char) != 1:
            print("You can only enter one character at a time, try again")
            continue
        if input_char in incorrect_guesses:
           print("You have already guessed that character, try again")
           continue
        guessed = False
        for i in range(len(list_of_characters)):
            if input_char == list_of_characters[i]:
                dict_of_stars["*"] = dict_of_stars["*"][:i] + input_char + dict_of_stars["*"][i+1:]
                guessed = True

        if guessed:
            print("Correct guess!")
        else:
            lifes -= 1
            incorrect_guesses += input_char
            print("Wrong guess, you have", lifes, "lives left")
            print("Incorrect guesses:", incorrect_guesses)

        print(dict_of_stars["*"])

        if "*" not in dict_of_stars["*"]:
            print("You won! The word was:", dict_of_stars["*"])
            break


hangman_word = input("Enter a word: ")
list_of_characters = list(hangman_word)
dict_of_stars = {"*": "*" * len(hangman_word)}  

hangman()

#Test
#Test2