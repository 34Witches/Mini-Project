import HalfAdder
import Or

class Adder():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.e = [0,]
        self.f = [0,]
        self.out = [0,]
        self.carry = [0,]
        self.gate0 = HalfAdder.HalfAdder()
        self.gate1 = HalfAdder.HalfAdder()
        self.gate2 = Or.Or()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._c = self.c
        self._d = self.d
        self._e = self.e
        self._f = self.f
        self.gate0.a = self._a
        self.gate0.b = self._b
        self.d = self.gate0.outf()
        self.e = self.gate0.carryf()
        self.gate1.a = self._c
        self.gate1.b = self._d
        self.out = self.gate1.outf()
        self.f = self.gate1.carryf()
        self.gate2.a = self._e
        self.gate2.b = self._f
        self.carry = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
    def carryf(self):
        self._setup()
        return self.carry
