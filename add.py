import itertools

# Add any size numbers, pass them in in as arrays
def add(n1, n2):
    l1 = len(n1)
    l2 = len(n2)
    c = 0
    sum = []
    for i, j in itertools.zip_longest(reversed(n1), reversed(n2)):
        s = int(i or 0) + int(j or 0) + c
        c = 1 if s >= 10 else 0
        sum.append(s if s < 10 else s - 10)
    sum.append(1 if c == 1 else 0)
    sum.reverse()
    print(sum)

add([5], [7])

add([9,6,2,3], [9,1,5,7])

add([1,6,3,3,5,7,3,5,9,7,8,9,0,5,6,7,8,5,6,3,3,5,7,8,9,3,8,7,6], [2,5,7,8,9,3,8,7,6,6,9,7,5,8,8,5,9,7,8,9,0,5,6,7,8,5,4,6,5,6])

add([9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])

