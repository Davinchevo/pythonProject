
name = input("Enter your name: ")


while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be less than 0")
    age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"Your age is {age} years old.")