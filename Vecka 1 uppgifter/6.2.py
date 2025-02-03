notes = { 1 : "George Washingtong",
         2 : "Thomas Jefferson",
         5 : "Abraham Lincoln",
         10 : "Alexander Hamilton",
         20 : "Andrew Jackson",
         50 : "Ulysses S. Grant",
         100 : "Benjamin Franklin"}

inputValue = int(input("Enter an amount! : "))

if inputValue in notes:
    print(notes[inputValue])
else:
    print("Wrong!")