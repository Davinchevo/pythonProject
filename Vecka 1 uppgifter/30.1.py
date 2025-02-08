def nextPrime(input_number):
    is_prime = False
    while not is_prime:
        input_number += 1
        if input_number % 2 != 0:
            return input_number



input_number = int(input("Enter a number: "))