def translate(sentence):
    
    vowels = "aeiouy"
    new_sentence = ""
    sentence_list = list(sentence)
    
    for character in sentence_list:
        
        if character.lower() not in vowels:
            character = f"{character}o{character}"
            new_sentence += character
        else:
            new_sentence += character

    return new_sentence

sentence = input("Enter a sentence: ")

print(translate(sentence))

