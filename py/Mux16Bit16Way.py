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
        self.gate0.a = self.a
        self.gate0.b = self.b
        self.gate0.c = self.c
        self.gate0.d = self.d
        self.gate0.e = self.e
        self.gate0.f = self.f
        self.gate0.g = self.g
        self.gate0.h = self.h
        self.gate0.select = self.select[1:4]
        self.q = self.gate0.outf()
        self.gate1.a = self.i
        self.gate1.b = self.j
        self.gate1.c = self.k
        self.gate1.d = self.l
        self.gate1.e = self.m
        self.gate1.f = self.n
        self.gate1.g = self.o
        self.gate1.h = self.p
        self.gate1.select = self.select[1:4]
        self.r = self.gate1.outf()
        self.gate2.a = self.q
        self.gate2.b = self.r
        self.gate2.select = self.select[0:1]
        self.out = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
