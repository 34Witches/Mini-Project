import Mux
import DFF

class Bit():
    def __init__(self):
        self.a = [0,]
        self.load = [0,]
        self.out = [0,]
        self.gate0 = Mux.Mux()
        self.gate1 = DFF.DFF()
    def _setup(self):
        self._a = self.a
        self._load = self.load
        self.gate0.a = self._c
        self.gate0.b = self._a
        self.gate0.select = self._load
        self.b = self.gate0.outf()
        self.gate1.a = self._b
        self.c = self.gate1.outf()
    def outf(self):
        self._setup()
        return self.out
