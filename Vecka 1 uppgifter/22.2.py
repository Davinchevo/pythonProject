def generate_n_chars(num, char):
    newStr = ""
    for i in range(num):
        newStr += char
    return newStr

print(generate_n_chars(5, "g"))