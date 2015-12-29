import Byte

class Word():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.load = [0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Byte.Byte()
        self.gate1 = Byte.Byte()
    def _setup(self):
        self.gate0.a = self.a[0:8]
        self.gate0.load = self.load
        self.out[0:8] = self.gate0.outf()
        self.gate1.a = self.a[8:16]
        self.gate1.load = self.load
        self.out[8:16] = self.gate1.outf()
    def outf(self):
        self._setup()
        return self.out
