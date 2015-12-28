import And

class And16Bit():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = And.And()
        self.gate1 = And.And()
        self.gate2 = And.And()
        self.gate3 = And.And()
        self.gate4 = And.And()
        self.gate5 = And.And()
        self.gate6 = And.And()
        self.gate7 = And.And()
        self.gate8 = And.And()
        self.gate9 = And.And()
        self.gate10 = And.And()
        self.gate11 = And.And()
        self.gate12 = And.And()
        self.gate13 = And.And()
        self.gate14 = And.And()
        self.gate15 = And.And()
    def _setup(self):
        self.gate0.a = self.a[0:1]
        self.gate0.b = self.b[0:1]
        self.out[0:1] = self.gate0.outf()
        self.gate1.a = self.a[1:2]
        self.gate1.b = self.b[1:2]
        self.out[1:2] = self.gate1.outf()
        self.gate2.a = self.a[2:3]
        self.gate2.b = self.b[2:3]
        self.out[2:3] = self.gate2.outf()
        self.gate3.a = self.a[3:4]
        self.gate3.b = self.b[3:4]
        self.out[3:4] = self.gate3.outf()
        self.gate4.a = self.a[4:5]
        self.gate4.b = self.b[4:5]
        self.out[4:5] = self.gate4.outf()
        self.gate5.a = self.a[5:6]
        self.gate5.b = self.b[5:6]
        self.out[5:6] = self.gate5.outf()
        self.gate6.a = self.a[6:7]
        self.gate6.b = self.b[6:7]
        self.out[6:7] = self.gate6.outf()
        self.gate7.a = self.a[7:8]
        self.gate7.b = self.b[7:8]
        self.out[7:8] = self.gate7.outf()
        self.gate8.a = self.a[8:9]
        self.gate8.b = self.b[8:9]
        self.out[8:9] = self.gate8.outf()
        self.gate9.a = self.a[9:10]
        self.gate9.b = self.b[9:10]
        self.out[9:10] = self.gate9.outf()
        self.gate10.a = self.a[10:11]
        self.gate10.b = self.b[10:11]
        self.out[10:11] = self.gate10.outf()
        self.gate11.a = self.a[11:12]
        self.gate11.b = self.b[11:12]
        self.out[11:12] = self.gate11.outf()
        self.gate12.a = self.a[12:13]
        self.gate12.b = self.b[12:13]
        self.out[12:13] = self.gate12.outf()
        self.gate13.a = self.a[13:14]
        self.gate13.b = self.b[13:14]
        self.out[13:14] = self.gate13.outf()
        self.gate14.a = self.a[14:15]
        self.gate14.b = self.b[14:15]
        self.out[14:15] = self.gate14.outf()
        self.gate15.a = self.a[15:]
        self.gate15.b = self.b[15:]
        self.out[15:] = self.gate15.outf()
    def outf(self):
        self._setup()
        return self.out
