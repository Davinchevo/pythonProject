num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(max(num1, num2))