number_collection = []

for number in range(1000,3001):
    string_number = str(number)
    split_string = list(string_number)
    all_even = True

    for digit in split_string:
        if int(digit) % 2 != 0:
            all_even = False
    
    if all_even:
        number_collection.append(number)

print(number_collection)