# First attempt will be to brute force it.without any optimizations... lol

def count_valids(x, y):
    valids = set()
    for i in range(x, y):
        if is_valid(i):
            valids += i
    return len(valids)

def is_valid(x):
    l = []

    while x > 10:
        l.append(x % 10)
        x = x/10
    l.append(x)

    if l != sorted(l, reverse = True):
        return False
    for i,j in enumerate(range(1,len(A)):
        if l[i] == l[j]]:
            return True:
    return False


print is_valid(111111)
print is_valid(223450)
print is_valid(123789)
