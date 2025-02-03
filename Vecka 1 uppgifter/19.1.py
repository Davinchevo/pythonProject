def reverse(input_string):
    reverse_string = ""
    for x in range(len(input_string) -1, -1 , -1):
        reverse_string += input_string[x]
    return reverse_string

input_string = input("Enter a string: ")

print(reverse(input_string))