import Not
import And16Bit
import Or16Bit

class Mux16Bit():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.select = [0,]
        self.invselect = [0,]
        self.select16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.invselect16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Not.Not()
        self.gate1 = And16Bit.And16Bit()
        self.gate2 = And16Bit.And16Bit()
        self.gate3 = Or16Bit.Or16Bit()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self._select = self.select
        self._invselect = self.invselect
        self._select16 = self.select16
        self._invselect16 = self.invselect16
        self._c = self.c
        self._d = self.d
        self.gate0.a = self._select
        self.invselect = self.gate0.outf()
        self.gate1.a = self._a
        self.gate1.b[0:1] = self._invselect
        self.gate1.b[1:2] = self._invselect
        self.gate1.b[2:3] = self._invselect
        self.gate1.b[3:4] = self._invselect
        self.gate1.b[4:5] = self._invselect
        self.gate1.b[5:6] = self._invselect
        self.gate1.b[6:7] = self._invselect
        self.gate1.b[7:8] = self._invselect
        self.gate1.b[8:9] = self._invselect
        self.gate1.b[9:10] = self._invselect
        self.gate1.b[10:11] = self._invselect
        self.gate1.b[11:12] = self._invselect
        self.gate1.b[12:13] = self._invselect
        self.gate1.b[13:14] = self._invselect
        self.gate1.b[14:15] = self._invselect
        self.gate1.b[15:16] = self._invselect
        self.c = self.gate1.outf()
        self.gate2.a = self._b
        self.gate2.b[0:1] = self._select
        self.gate2.b[1:2] = self._select
        self.gate2.b[2:3] = self._select
        self.gate2.b[3:4] = self._select
        self.gate2.b[4:5] = self._select
        self.gate2.b[5:6] = self._select
        self.gate2.b[6:7] = self._select
        self.gate2.b[7:8] = self._select
        self.gate2.b[8:9] = self._select
        self.gate2.b[9:10] = self._select
        self.gate2.b[10:11] = self._select
        self.gate2.b[11:12] = self._select
        self.gate2.b[12:13] = self._select
        self.gate2.b[13:14] = self._select
        self.gate2.b[14:15] = self._select
        self.gate2.b[15:16] = self._select
        self.d = self.gate2.outf()
        self.gate3.a = self._c
        self.gate3.b = self._d
        self.out = self.gate3.outf()
    def outf(self):
        self._setup()
        return self.out
