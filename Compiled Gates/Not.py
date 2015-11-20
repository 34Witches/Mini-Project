import Nand

class Not():
    def __init__(self):
        self.a = [0,]
        self.out = [0,]
        self.gate0 = Nand.Nand()
    def _setup(self):
        self._a = self.a
        self.gate0.a = self._a
        self.gate0.b = self._a
        self.out = self.gate0.outf()
    def outf(self):
        self._setup()
        return self.out
