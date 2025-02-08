def filter_long_words(words, n):
    longer_words = ""
    for word in words:
        if len(word) > n:
            longer_words += word + ","

    return longer_words

print(filter_long_words(["hej", "hejsan", "hejsanhejsan", "hejsanhejsanhejsan"], 5))