import Or

class Or16Bit():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Or.Or()
        self.gate1 = Or.Or()
        self.gate2 = Or.Or()
        self.gate3 = Or.Or()
        self.gate4 = Or.Or()
        self.gate5 = Or.Or()
        self.gate6 = Or.Or()
        self.gate7 = Or.Or()
        self.gate8 = Or.Or()
        self.gate9 = Or.Or()
        self.gate10 = Or.Or()
        self.gate11 = Or.Or()
        self.gate12 = Or.Or()
        self.gate13 = Or.Or()
        self.gate14 = Or.Or()
        self.gate15 = Or.Or()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self.gate0.a = self._a[0:1]
        self.gate0.b = self._b[0:1]
        self.out[0:1] = self.gate0.outf()
        self.gate1.a = self._a[1:2]
        self.gate1.b = self._b[1:2]
        self.out[1:2] = self.gate1.outf()
        self.gate2.a = self._a[2:3]
        self.gate2.b = self._b[2:3]
        self.out[2:3] = self.gate2.outf()
        self.gate3.a = self._a[3:4]
        self.gate3.b = self._b[3:4]
        self.out[3:4] = self.gate3.outf()
        self.gate4.a = self._a[4:5]
        self.gate4.b = self._b[4:5]
        self.out[4:5] = self.gate4.outf()
        self.gate5.a = self._a[5:6]
        self.gate5.b = self._b[5:6]
        self.out[5:6] = self.gate5.outf()
        self.gate6.a = self._a[6:7]
        self.gate6.b = self._b[6:7]
        self.out[6:7] = self.gate6.outf()
        self.gate7.a = self._a[7:8]
        self.gate7.b = self._b[7:8]
        self.out[7:8] = self.gate7.outf()
        self.gate8.a = self._a[8:9]
        self.gate8.b = self._b[8:9]
        self.out[8:9] = self.gate8.outf()
        self.gate9.a = self._a[9:10]
        self.gate9.b = self._b[9:10]
        self.out[9:10] = self.gate9.outf()
        self.gate10.a = self._a[10:11]
        self.gate10.b = self._b[10:11]
        self.out[10:11] = self.gate10.outf()
        self.gate11.a = self._a[11:12]
        self.gate11.b = self._b[11:12]
        self.out[11:12] = self.gate11.outf()
        self.gate12.a = self._a[12:13]
        self.gate12.b = self._b[12:13]
        self.out[12:13] = self.gate12.outf()
        self.gate13.a = self._a[13:14]
        self.gate13.b = self._b[13:14]
        self.out[13:14] = self.gate13.outf()
        self.gate14.a = self._a[14:15]
        self.gate14.b = self._b[14:15]
        self.out[14:15] = self.gate14.outf()
        self.gate15.a = self._a[15:]
        self.gate15.b = self._b[15:]
        self.out[15:] = self.gate15.outf()
    def outf(self):
        self._setup()
        return self.out
