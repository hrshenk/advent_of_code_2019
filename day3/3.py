class Wire:
    def __init__(self, path):
        self.path = path
        self.points = set()
        self.current = [0,0]

    def generate_points(self):
        for entry in self.path:
            self.add_points(entry)
        return self.points

    def add_points(self, entry):
        index = 0 if entry[0] in {'R', 'L'} else 1
        direction = 1 if entry[0] in {'R', 'U'} else -1
        magnitude = int(entry[1:])
        current = self.current
        for i in range(magnitude):
            current[index] += direction
            self.points.add(tuple(current))

def manhattan(x):
    d = 0
    for entry in x:
        d += abs(entry)
    return d

# Part 1
with open("input.txt", 'r') as f:
    wire1 = f.readline().split(',')
    wire2 =f.readline().split(',')


w = Wire(wire1)
set1 = w.generate_points()

w = Wire(wire2)
set2 = w.generate_points()

intersection = set1 & set2

res = min(intersection, key=manhattan)

print("Part 1: %d" % manhattan(res))
