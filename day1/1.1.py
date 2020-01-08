total = 0

def fuel_required(x):
    return x/3 - 2

with open("input.txt", 'r') as f:
    for line in f:
        total += fuel_required(int(line))

print total
print fuel_required(100756)
print fuel_required(1969)
