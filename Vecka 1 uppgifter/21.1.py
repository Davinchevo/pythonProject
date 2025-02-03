def overlapping1(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

def overlapping2(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def main():
    list1 = [1,2,3,4]
    list2 = [4,5,6,7]
    print(overlapping1(list1, list2))
    print(overlapping2(list1, list2))

main()