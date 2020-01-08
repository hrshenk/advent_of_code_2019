import itertools
import copy

class Computer:
    def __init__(self, program):
        self.program = copy.copy(program)
        self.instruction_width = 4

    def eval(self):
        iwidth = self.instruction_width
        program = self.program
        pad = [0] * (-len(program) % iwidth)
        program += pad
        row_count = len(program)/iwidth
        for i in range(row_count):
            row_index = i * iwidth
            row = program[row_index:row_index+iwidth]
            if row[0] == 99:
                program = program[:-len(pad)]
                return program
            elif row[0] == 1:
                f = self.add
            elif row[0] == 2:
                f = self.multiply
            else:
                raise ValueError("Invalid opcode %d at index %d" % (row[0], i*iwidth))

            program[row[3]] = f(program[row[1]], program[row[2]])
	    print row[1:]


    def multiply(self, a, b):
        return a*b

    def add(self, a, b):
        return a+b


with open("input.txt") as f:
    l = f.readline().split(',')
    l = [int(x) for x in l]

# part 1
l[1] = 12
l[2] = 2
c = Computer(l)
res = c.eval()
print("Part 1: %d" % res[0])
print res[-10:]
print res[151]
print res[13]
print res[0]

#part 2
# target = 19690720

# for noun, verb in itertools.product(range(100), range(100)):
#     #initialize the program
#     l[1] = noun
#     l[2] = verb
#     #load the program
#     c = Computer(l)
#     # run the program
#     res = c.eval()
#     if res[0] == target:
#         res = 100 * noun + verb
#         print("Part 2: %d" % res)
#         exit()
