def generate_n_chars(n, c):  # Function takes two inputs: n (number) and c (character)
    newStr = ""  # Start with an empty string
    for i in range(n):  # Loop 'n' times
        newStr += c  # Add character 'c' to newStr each time
    return newStr  # Return the final string

print(generate_n_chars(5, "x"))  # Call function with 5 and "x"
