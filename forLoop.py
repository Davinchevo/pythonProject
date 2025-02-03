#First value is inclusive, second value is exclusive, third value is the incremented value
for i in range(1, 11, 2):
    print(i)


name = "David Johansson"

for letter in name:
    print(letter, end="-")


for i in range(10,-1, -1):
    print(i)
    if i == 0:
        print("Happy New Year!")