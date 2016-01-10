import Bit

class RAM256():
    def __init__(self):
        self.a = [0 for i in range(16)]
        self.load = [0]
        self.select = [0 for i in range(8)]
        self.out = [0 for i in range(16)]
        self.memory = [[0 for i in range(16)] for i in range(256)]
        Bit.Bit.clocked.append(self)

    def update(self):
        accessed = int(''.join(map(str, self.select)), 2)
        if self.load[0]:
            self.memory[accessed] = self.a
        self.out = self.memory[accessed]

    def outf(self):
        return self.out
