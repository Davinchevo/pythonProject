def find_longest_word(list_of_words):
    longest_word = ""
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(find_longest_word(["hej", "hejsan", "hejsanhejsan", "hejsanhejsanhejsan"]))