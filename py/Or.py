import Not
import Nand

class Or():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.out = [0,]
        self.gate0 = Not.Not()
        self.gate1 = Not.Not()
        self.gate2 = Nand.Nand()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._c = self.c
        self._d = self.d
        self.gate0.a = self._a
        self.c = self.gate0.outf()
        self.gate1.a = self._b
        self.d = self.gate1.outf()
        self.gate2.a = self._c
        self.gate2.b = self._d
        self.out = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
