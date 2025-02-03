
notes = {
"1" : "George Washington",
"2" : "Thomas Jefferson",
"5" : "Abraham Lincoln",
"10" : "Alexander Hamilton",
"20" : "Andrew Jackson",
"50" : "Ulysses S. Grant",
"100" : "Benjamin Franklin"}

value = input("Enter the amount of numbers you want to input: ")

if value not in notes:
    print("Invalid amount")

else:
    print(notes[value])


