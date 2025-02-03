# List[] = mutable, most flexible
# Tuple() = immutable, faster
# Set{} = mutable (add/remove), unordered, no duplicates, best for membership testing



fruits = ["apple", "orange", "banana", "coconut"]

for fruit in fruits:
    print(fruit, end="")

# fruits[0] = "mango"
# fruits.append("mango")
# fruits.remove("banana")
# fruits.pop(0) - #Pop gets rid of the specific element at the index position
# fruits.clear()

fruits.add("pear")

# Below works well for Sets.
if "apple" in fruits:
    print("Apple was found")
else:
    print("Apple was not found")

fruit = input("Input the fruit you are searching for: ")

for fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")