import Mux16Bit

class Mux16Bit4Way():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.select = [0,0,]
        self.e = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Mux16Bit.Mux16Bit()
        self.gate1 = Mux16Bit.Mux16Bit()
        self.gate2 = Mux16Bit.Mux16Bit()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._c = self.c
        self._d = self.d
        self._select = self.select
        self._e = self.e
        self._f = self.f
        self.gate0.a = self._a
        self.gate0.b = self._b
        self.gate0.select = self._select[1:2]
        self.e = self.gate0.outf()
        self.gate1.a = self._c
        self.gate1.b = self._d
        self.gate1.select = self._select[1:2]
        self.f = self.gate1.outf()
        self.gate2.a = self._e
        self.gate2.b = self._f
        self.gate2.select = self._select[0:1]
        self.out = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
