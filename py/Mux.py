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
        self._a = self.a
        self._b = self.b
        self._select = self.select
        self._c = self.c
        self._d = self.d
        self._invselect = self.invselect
        self.gate0.a = self._select
        self.invselect = self.gate0.outf()
        self.gate1.a = self._a
        self.gate1.b = self._invselect
        self.c = self.gate1.outf()
        self.gate2.a = self._b
        self.gate2.b = self._select
        self.d = self.gate2.outf()
        self.gate3.a = self._c
        self.gate3.b = self._d
        self.out = self.gate3.outf()
    def outf(self):
        self._setup()
        return self.out
