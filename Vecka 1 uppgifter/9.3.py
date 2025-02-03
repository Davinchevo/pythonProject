vowels = "aeiouy"

input_string = input("Enter a string: ")
result_string = ""

for letter in input_string:
    if letter in vowels:
        result_string += letter.upper()
    else:
        result_string += letter


print(result_string)