first = 5
second = -1
third = 3

def max_of_three(first, second, third):
    if first > second and first > third:
        return first
    elif second > first and second > third:
        return second
    else:
        return third
    
def main():
    biggest = max_of_three(3, 6, -5)
    print(biggest)

main()