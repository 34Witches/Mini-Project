import Xor

class AdderEnd():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.out = [0,]
        self.gate0 = Xor.Xor()
        self.gate1 = Xor.Xor()
    def _setup(self):
        self.gate0.a = self.a
        self.gate0.b = self.b
        self.d = self.gate0.outf()
        self.gate1.a = self.c
        self.gate1.b = self.d
        self.out = self.gate1.outf()
    def outf(self):
        self._setup()
        return self.out
