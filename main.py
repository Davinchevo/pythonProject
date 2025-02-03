#This is my first Python program
print("I like tacos!")
print("It's really good")

#Variable
full_name = "David Johansson"
age = 34
gpa = 3.2
is_student = False

print(f"Hello {full_name}")
print(f"You are {age} years old")
print(f"Your GPA is {gpa}")
print(f"Are you a student?: {is_student}")
 
 #Arithmetic

friends = 5

remaining_friends = friends % 3

friends -= 2
friends += 1
friends *= 4
friends /= 2

#Integer division // = returnerar ett heltal
friends //= 2

print(f"Amount of friend: {friends}")
print(f"Remaining friends: {remaining_friends}")


#If-statement

if  is_student:
    print("You are a student")
else:
    print("You are not a student")

#Typecasting

name = "David Johansson"
age = 34
gpa = 3.2
is_student = True

gpa = int(gpa)
age = float(age)

print(type(gpa))