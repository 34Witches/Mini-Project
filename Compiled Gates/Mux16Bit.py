import Not
import And16Bit
import Or16Bit

class Mux16Bit():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.select = [0,]
        self.invselect = [0,]
        self.select16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.invselect16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Not.Not()
        self.gate1 = And16Bit.And16Bit()
        self.gate2 = And16Bit.And16Bit()
        self.gate3 = Or16Bit.Or16Bit()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._select = self.select
        self._invselect = self.invselect
        self._select16 = self.select16
        self._invselect16 = self.invselect16
        self._c = self.c
        self._d = self.d
        self.gate0.a = self._select
        self.invselect = self.gate0.outf()
        self.select16 = (self.select)*16
        self.invselect16 = (self.invselect)*16
        self.gate1.a = self._a
        self.gate1.b = self._invselect16
        self.c = self.gate1.outf()
        self.gate2.a = self._b
        self.gate2.b = self._select16
        self.d = self.gate2.outf()
        self.gate3.a = self._c
        self.gate3.b = self._d
        self.out = self.gate3.outf()
    def outf(self):
        self._setup()
        return self.out
