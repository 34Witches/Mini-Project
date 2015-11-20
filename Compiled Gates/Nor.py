import Or
import Not

class Nor():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.c = [0,]
        self.out = [0,]
        self.gate0 = Or.Or()
        self.gate1 = Not.Not()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._c = self.c
        self.gate0.a = self._a
        self.gate0.b = self._b
        self.c = self.gate0.outf()
        self.gate1.a = self._c
        self.out = self.gate1.outf()
    def outf(self):
        self._setup()
        return self.out
