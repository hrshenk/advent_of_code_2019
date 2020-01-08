total = 0

def fuel_required(x):
    res = x/3-2
    if res > 0:
        return res + fuel_required(res)
    return 0

with open("input.txt", 'r') as f:
    for line in f:
        total += fuel_required(int(line))

print total
print fuel_required(100756)
print fuel_required(1969)
