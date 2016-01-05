import Mux

class Mux4Way():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.select = [0,0,]
        self.out = [0,]
        self.gate0 = Mux.Mux()
        self.gate1 = Mux.Mux()
        self.gate2 = Mux.Mux()
    def _setup(self):
        self.gate0.a = self.a
        self.gate0.b = self.b
        self.gate0.select = self.select[1:2]
        self.e = self.gate0.outf()
        self.gate1.a = self.c
        self.gate1.b = self.d
        self.gate1.select = self.select[1:2]
        self.f = self.gate1.outf()
        self.gate2.a = self.e
        self.gate2.b = self.f
        self.gate2.select = self.select[0:1]
        self.out = self.gate2.outf()
    def outf(self):
        self._setup()
        return self.out
