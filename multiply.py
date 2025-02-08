import itertools
from add import add

# Multiply any size numbers, pass them in in as arrays
def multiply(n1, n2):
    l1 = len(n1)
    l2 = len(n2)
    if l1 < l2:
        n1,n2 = n2,n1
    
    products = []
    for idx, j in enumerate(reversed(n2)):
        c = 0
        product = [0] * idx
        for i in reversed(n1):
            p = int(i) * int(j) + int(c)
            c = int((str(p))[0]) if p >= 10 else 0
            product.append(p if p < 10 else p % 10)
        product.append(c if c >= 1 else 0)
        product.reverse()
        products.append(product)
    
    result = [0]
    for i in products:
        result = add(result, i)
    return result

# print(multiply([9,6], [4,2]))

# print(multiply([9,1,2,6], [4,6,7,2]))

# print(multiply([9,4,7,3,2,6,3,6,2,7,8,4,7,9,4,6,7,4,3,6,8,3,4,1,2,6], [4,6,3,2,6,3,6,2,7,8,4,7,9,4,6,7,4,3,7,2]))
