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
        self.gate0.a = self.select
        self.invselect = self.gate0.outf()
        self.gate1.a = self.a
        self.gate1.b[0:1] = self.invselect
        self.gate1.b[1:2] = self.invselect
        self.gate1.b[2:3] = self.invselect
        self.gate1.b[3:4] = self.invselect
        self.gate1.b[4:5] = self.invselect
        self.gate1.b[5:6] = self.invselect
        self.gate1.b[6:7] = self.invselect
        self.gate1.b[7:8] = self.invselect
        self.gate1.b[8:9] = self.invselect
        self.gate1.b[9:10] = self.invselect
        self.gate1.b[10:11] = self.invselect
        self.gate1.b[11:12] = self.invselect
        self.gate1.b[12:13] = self.invselect
        self.gate1.b[13:14] = self.invselect
        self.gate1.b[14:15] = self.invselect
        self.gate1.b[15:16] = self.invselect
        self.c = self.gate1.outf()
        self.gate2.a = self.b
        self.gate2.b[0:1] = self.select
        self.gate2.b[1:2] = self.select
        self.gate2.b[2:3] = self.select
        self.gate2.b[3:4] = self.select
        self.gate2.b[4:5] = self.select
        self.gate2.b[5:6] = self.select
        self.gate2.b[6:7] = self.select
        self.gate2.b[7:8] = self.select
        self.gate2.b[8:9] = self.select
        self.gate2.b[9:10] = self.select
        self.gate2.b[10:11] = self.select
        self.gate2.b[11:12] = self.select
        self.gate2.b[12:13] = self.select
        self.gate2.b[13:14] = self.select
        self.gate2.b[14:15] = self.select
        self.gate2.b[15:16] = self.select
        self.d = self.gate2.outf()
        self.gate3.a = self.c
        self.gate3.b = self.d
        self.out = self.gate3.outf()
    def outf(self):
        self._setup()
        return self.out
