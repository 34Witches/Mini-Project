import Or
import Nand
import And

class Xor():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.out = [0,]
        self.gate0 = Or.Or()
        self.gate1 = Nand.Nand()
        self.gate2 = And.And()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._c = self.c
        self._d = self.d
        self.gate0.a = self._a
        self.gate0.b = self._b
        self.c = self.gate0.outf()
        self.gate1.a = self._a
        self.gate1.b = self._b
        self.d = self.gate1.outf()
        self.gate2.a = self._c
        self.gate2.b = self._d
        self.out = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
