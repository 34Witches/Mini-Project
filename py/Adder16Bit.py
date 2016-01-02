import HalfAdder
import Adder
import AdderEnd

class Adder16Bit():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.c1 = [0,]
        self.c2 = [0,]
        self.c3 = [0,]
        self.c4 = [0,]
        self.c5 = [0,]
        self.c6 = [0,]
        self.c7 = [0,]
        self.c8 = [0,]
        self.c9 = [0,]
        self.c10 = [0,]
        self.c11 = [0,]
        self.c12 = [0,]
        self.c13 = [0,]
        self.c14 = [0,]
        self.c15 = [0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = HalfAdder.HalfAdder()
        self.gate1 = Adder.Adder()
        self.gate2 = Adder.Adder()
        self.gate3 = Adder.Adder()
        self.gate4 = Adder.Adder()
        self.gate5 = Adder.Adder()
        self.gate6 = Adder.Adder()
        self.gate7 = Adder.Adder()
        self.gate8 = Adder.Adder()
        self.gate9 = Adder.Adder()
        self.gate10 = Adder.Adder()
        self.gate11 = Adder.Adder()
        self.gate12 = Adder.Adder()
        self.gate13 = Adder.Adder()
        self.gate14 = Adder.Adder()
        self.gate15 = AdderEnd.AdderEnd()
    def _setup(self):
        self.gate0.a = self.a[0:1]
        self.gate0.b = self.b[0:1]
        self.out[0:1] = self.gate0.outf()
        self.c1 = self.gate0.carryf()
        self.gate1.a = self.a[1:2]
        self.gate1.b = self.b[1:2]
        self.gate1.c = self.c1
        self.out[1:2] = self.gate1.outf()
        self.c2 = self.gate1.carryf()
        self.gate2.a = self.a[2:3]
        self.gate2.b = self.b[2:3]
        self.gate2.c = self.c2
        self.out[2:3] = self.gate2.outf()
        self.c3 = self.gate2.carryf()
        self.gate3.a = self.a[3:4]
        self.gate3.b = self.b[3:4]
        self.gate3.c = self.c3
        self.out[3:4] = self.gate3.outf()
        self.c4 = self.gate3.carryf()
        self.gate4.a = self.a[4:5]
        self.gate4.b = self.b[4:5]
        self.gate4.c = self.c4
        self.out[4:5] = self.gate4.outf()
        self.c5 = self.gate4.carryf()
        self.gate5.a = self.a[5:6]
        self.gate5.b = self.b[5:6]
        self.gate5.c = self.c5
        self.out[5:6] = self.gate5.outf()
        self.c6 = self.gate5.carryf()
        self.gate6.a = self.a[6:7]
        self.gate6.b = self.b[6:7]
        self.gate6.c = self.c6
        self.out[6:7] = self.gate6.outf()
        self.c7 = self.gate6.carryf()
        self.gate7.a = self.a[7:8]
        self.gate7.b = self.b[7:8]
        self.gate7.c = self.c7
        self.out[7:8] = self.gate7.outf()
        self.c8 = self.gate7.carryf()
        self.gate8.a = self.a[8:9]
        self.gate8.b = self.b[8:9]
        self.gate8.c = self.c8
        self.out[8:9] = self.gate8.outf()
        self.c9 = self.gate8.carryf()
        self.gate9.a = self.a[9:10]
        self.gate9.b = self.b[9:10]
        self.gate9.c = self.c9
        self.out[9:10] = self.gate9.outf()
        self.c10 = self.gate9.carryf()
        self.gate10.a = self.a[10:11]
        self.gate10.b = self.b[10:11]
        self.gate10.c = self.c10
        self.out[10:11] = self.gate10.outf()
        self.c11 = self.gate10.carryf()
        self.gate11.a = self.a[11:12]
        self.gate11.b = self.b[11:12]
        self.gate11.c = self.c11
        self.out[11:12] = self.gate11.outf()
        self.c12 = self.gate11.carryf()
        self.gate12.a = self.a[12:13]
        self.gate12.b = self.b[12:13]
        self.gate12.c = self.c12
        self.out[12:13] = self.gate12.outf()
        self.c13 = self.gate12.carryf()
        self.gate13.a = self.a[13:14]
        self.gate13.b = self.b[13:14]
        self.gate13.c = self.c13
        self.out[13:14] = self.gate13.outf()
        self.c14 = self.gate13.carryf()
        self.gate14.a = self.a[14:15]
        self.gate14.b = self.b[14:15]
        self.gate14.c = self.c14
        self.out[14:15] = self.gate14.outf()
        self.c15 = self.gate14.carryf()
        self.gate15.a = self.a[15:16]
        self.gate15.b = self.b[15:16]
        self.gate15.c = self.c15
        self.out[15:16] = self.gate15.outf()
    def outf(self):
        self._setup()
        return self.out
