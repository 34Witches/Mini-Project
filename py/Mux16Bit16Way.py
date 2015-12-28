import Mux16Bit8Way
import Mux16Bit

class Mux16Bit16Way():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.e = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.g = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.h = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.i = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.j = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.l = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.m = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.n = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.o = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.p = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.select = [0,0,0,0,]
        self.q = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Mux16Bit8Way.Mux16Bit8Way()
        self.gate1 = Mux16Bit8Way.Mux16Bit8Way()
        self.gate2 = Mux16Bit.Mux16Bit()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._c = self.c
        self._d = self.d
        self._e = self.e
        self._f = self.f
        self._g = self.g
        self._h = self.h
        self._i = self.i
        self._j = self.j
        self._k = self.k
        self._l = self.l
        self._m = self.m
        self._n = self.n
        self._o = self.o
        self._p = self.p
        self._select = self.select
        self._q = self.q
        self._r = self.r
        self.gate0.a = self._a
        self.gate0.b = self._b
        self.gate0.c = self._c
        self.gate0.d = self._d
        self.gate0.e = self._e
        self.gate0.f = self._f
        self.gate0.g = self._g
        self.gate0.h = self._h
        self.gate0.select = self._select[1:4]
        self.q = self.gate0.outf()
        self.gate1.a = self._i
        self.gate1.b = self._j
        self.gate1.c = self._k
        self.gate1.d = self._l
        self.gate1.e = self._m
        self.gate1.f = self._n
        self.gate1.g = self._o
        self.gate1.h = self._p
        self.gate1.select = self._select[1:4]
        self.r = self.gate1.outf()
        self.gate2.a = self._q
        self.gate2.b = self._r
        self.gate2.select = self._select[0:1]
        self.out = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
