import Bit

class InstructionMemory():
    def __init__(self):
        self.memory = [[0 for i in range(16)] for i in range(2**15)]
        self.select = [0 for i in range(15)]
        self.out = [0 for i in range(16)]
        instructions = open("program.asm", 'r')
        for i, j in enumerate(instructions.readlines())
            self.memory[i] = list(map(int, list(j.rstrip('\n'))))
        instructions.close()
        Bit.Bit.bits.append(self)

    def update(self):
        i = 0
        for j, k in enumerate(self.select):
            i += ((2**(14-j))*k)
        self.out = self.memory[i]

    def outf(self):
        return self.out
