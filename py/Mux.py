import Not
import And
import Or

class Mux():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.select = [0,]
        self.c = [0,]
        self.d = [0,]
        self.invselect = [0,]
        self.out = [0,]
        self.gate0 = Not.Not()
        self.gate1 = And.And()
        self.gate2 = And.And()
        self.gate3 = Or.Or()
    def _setup(self):
        self.gate0.a = self.select
        self.invselect = self.gate0.outf()
        self.gate1.a = self.a
        self.gate1.b = self.invselect
        self.c = self.gate1.outf()
        self.gate2.a = self.b
        self.gate2.b = self.select
        self.d = self.gate2.outf()
        self.gate3.a = self.c
        self.gate3.b = self.d
        self.out = self.gate3.outf()
    def outf(self):
        self._setup()
        return self.out
