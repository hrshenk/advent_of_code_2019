# First attempt will be to brute force it without any optimizations... lol

def count_valids(x, y):
    valids = []
    for i in range(x, y):
        if is_valid(i):
            valids.append(i)
    return len(valids)

def is_valid(x):
    l = []

    while x > 10:
        l.append(x % 10)
        x = x/10
    l.append(x)

    if l != sorted(l, reverse = True):
        return False

    i = 0
    run = 1

    while i < len(l)-1:
        if l[i] == l[i+1]:
            run += 1
        else:
            if run == 2:
                break
            else:
                run = 1
        i += 1
    return run == 2

print(count_valids(246540, 787419))
