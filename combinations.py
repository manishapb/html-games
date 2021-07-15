from itertools import combinations

def find_combination(array, n, pred):
    combs = combinations(array,n)
    for c in combs:
        if pred(c):
            return c


array = [12,3,4,9,1,2,8,6]

def product(xs):
    res = 1
    for x in xs:
        res = res*x

    return res

print(find_combination(array, 3, lambda c: product(c)==18))
