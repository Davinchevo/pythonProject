def sum(additions):
    sum = 0
    for x in additions:
        sum += x
    return sum

def multiply(multiplicands):
    product = 0
    for x in multiplicands:
        if product == 0:
            product += x
        else:
            product *= x
    return product


additions = [1,2,3,4,5]
print(sum(additions))
multiplicands = [1,2,3,4,5]
print(multiply(multiplicands))
