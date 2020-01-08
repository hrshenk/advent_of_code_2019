class Wire:
    def __init__(self, path):
        self.path = path
        self.points = {}
        self.current = [0,0]
        self.steps = 0
    def generate_points(self):
        for entry in self.path:
            self.add_points(entry)
        return self.points

    def add_points(self, entry):
        index = 0 if entry[0] in {'R', 'L'} else 1
        direction = 1 if entry[0] in {'R', 'U'} else -1
        magnitude = int(entry[1:])
        current = self.current
        points = self.points

        for i in range(magnitude):
            current[index] += direction
            self.steps += 1
            point = tuple(current)
            if point not in points:
                points[point] = self.steps
        return points

with open("input.txt", 'r') as f:
    wire1 = f.readline().split(',')
    wire2 =f.readline().split(',')

#wire1 = "R8,U5,L5,D3".split(',')
#wire2 = "U7,R6,D4,L4".split(',')

w = Wire(wire1)
h1 = w.generate_points()

w = Wire(wire2)
h2 = w.generate_points()

intersection = [x for x in h1.keys() if x in h2]

res = min(intersection, key=lambda x: h1[x] + h2[x])

res = h1[res] + h2[res]
print(res)
