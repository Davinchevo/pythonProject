def myLen(iterable):
    count = 0
    for x in iterable:
        count += 1
    return count

myStr = "Hello, World!"
print(myLen(myStr))

myList = [1,2,3,4,5]
print(myLen(myList))

mySet = {1,2,3,4,5,6}
print(myLen(mySet))