class PC():
    def __init__(self):
        self.counter = 0
        self.a = [0 for i in range(15)]
        self.inc = [0]
        self.load = [0]
        self.reset = [0]
        self.out = [0 for i in range(15)]

    def _setup(self):
        if self.reset[0]:
            self.counter = 0
        elif self.load[0]:
            self.counter = 0
            for i, j in enumerate(self.a):
                self.counter += ((2**(14-i))*j)
        elif self.inc[0]:
            self.counter += 1
        self.out = list(map(int, list(bin(self.counter)[2:])))
        if len(self.out) != 15:
            self.out = [0 for i in range(16 - len(self.out))] + self.out

    def outf(self):
        self._setup()
        return self.out
