import itertools
import copy
from collections import deque

class Computer:
    def __init__(self, program):
        self.program = copy.copy(program)
        self.program += 4096*[0]

        # registers
        self.pc = 0
        self.args = []
        self.jump = False
        self.iters = 0
        self.in_queue = deque()
        self._output = None
        self.relative_base = 0

        # opcode metadata
        # opcode:(argument count, supports_immediate,....)
        self.arg_counts = {1:(3,1,1,0),\
                           2:(3,1,1,0),\
                           3:(1,1),\
                           4:(1,1),\
                           5:(2,1,1),\
                           6:(2,1,1),\
                           7:(3,1,1,0),\
                           8:(3,1,1,0),\
                           9:(1,1),\
                           99:tuple([0])}

        self.opcode_methods = {1:self.add,\
                               2:self.multiply,\
                               3:self.input_value,\
                               4:self.output_value,\
                               5:self.jump_true,\
                               6:self.jump_false,\
                               7:self.less,\
                               8:self.equals,\
                               9:self.adjust_base,\
                               99:self.halt}

    @property
    def output(self):
        return self._output

    def queue_input(self, string):
        self.in_queue.appendleft(str(string))

    def eval(self):
        self.scheduled = True

        while self.scheduled:
            self.fetch_and_exec()
            # increment pc where appropriate
            if not self.jump:
                self.pc += len(self.args)+1
            self.jump = False

        return self.program

    def fetch_and_exec(self):
        pc = self.pc
        program = self.program

        # fetch opcode
        modes, opcode = divmod(program[pc], 100)
        # decode
        self.args = self.get_args(modes,opcode)
        # execute
        self.execute(opcode)

    def get_args(self, modes, opcode):
        args = []
        argc = self.arg_counts[opcode]
        pc = self.pc
        relative_base = self.relative_base
        program = self.program

        for i in range(1,len(argc)):
            a = self.program[pc + i]
            if modes % 10 == 1 or not argc[i]: # immediate mode
                args.append(a)
            elif modes % 10 == 2: # relative mode
                args.append(program[relative_base + a])
            else:
                args.append(program[a])
            modes = modes//10
        return args

    def multiply(self):
        if len(self.args) != 3:
            raise ValueError("Wrong arg count")
        a, b, i = self.args[:]
        self.program[i] = a*b

    def add(self):
        if len(self.args) != 3:
            raise ValueError("Wrong arg count")
        a, b, i = self.args[:]
        self.program[i] = a+b

    def output_value(self):
        self._output = self.args[0]
        print(f"output: {self.args[0]}")

    def input_value(self):
        if len(self.args) != 1:
            raise ValueError("Wrong arg count")
        if self.in_queue:
            x = self.in_queue.pop()
        else:
            x = input("Enter value:")
        self.program[self.args[0]] = int(x)

    def jump_true(self):
        if len(self.args) != 2:
            raise ValueError("Wrong arg count")
        if self.args[0]:
            self.pc = self.args[1]
            self.jump = True

    def jump_false(self):
        if len(self.args) != 2:
            raise ValueError("Wrong self.args count")
        self.args[0] = not self.args[0]
        self.jump_true()

    def less(self):
        if len(self.args) != 3:
            raise ValueError("Wrong self.args count")
        a, b, i = self.args[:]
        self.program[i] = 1 if a < b else 0

    def equals(self):
        if len(self.args) != 3:
            raise ValueError("Wrong self.args count")
        a, b, i = self.args[:]
        self.program[i] = 1 if a == b else 0

    def adjust_base(self):
        if len(self.args) != 1:
            raise ValueError("Wrong self.args count")
        self.relative_base += self.args[0]

    def halt(self):
        if len(self.args) != 0:
            raise ValueError("Wrong arg count")
        self.scheduled = False

    def execute(self, opcode):
        f = self.opcode_methods[opcode]
        f()

with open("input.txt") as f:
    l = f.readline().split(',')
    l = [int(x) for x in l]

c = Computer(l)

c.eval()
