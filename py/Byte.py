import Bit

class Byte():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,]
        self.load = [0,]
        self.out = [0,0,0,0,0,0,0,0,]
        self.gate0 = Bit.Bit()
        self.gate1 = Bit.Bit()
        self.gate2 = Bit.Bit()
        self.gate3 = Bit.Bit()
        self.gate4 = Bit.Bit()
        self.gate5 = Bit.Bit()
        self.gate6 = Bit.Bit()
        self.gate7 = Bit.Bit()
    def _setup(self):
        self._a = self.a
        self._load = self.load
        self.gate0.a = self._a[0:1]
        self.gate0.load = self._load
        self.out[0:1] = self.gate0.outf()
        self.gate1.a = self._a[1:2]
        self.gate1.load = self._load
        self.out[1:2] = self.gate1.outf()
        self.gate2.a = self._a[2:3]
        self.gate2.load = self._load
        self.out[2:3] = self.gate2.outf()
        self.gate3.a = self._a[3:4]
        self.gate3.load = self._load
        self.out[3:4] = self.gate3.outf()
        self.gate4.a = self._a[4:5]
        self.gate4.load = self._load
        self.out[4:5] = self.gate4.outf()
        self.gate5.a = self._a[5:6]
        self.gate5.load = self._load
        self.out[5:6] = self.gate5.outf()
        self.gate6.a = self._a[6:7]
        self.gate6.load = self._load
        self.out[6:7] = self.gate6.outf()
        self.gate7.a = self._a[7:8]
        self.gate7.load = self._load
        self.out[7:8] = self.gate7.outf()
    def outf(self):
        self._setup()
        return self.out
