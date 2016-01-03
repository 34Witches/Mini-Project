import Or
import Not

class IsZero():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.e = [0,]
        self.f = [0,]
        self.g = [0,]
        self.h = [0,]
        self.i = [0,]
        self.j = [0,]
        self.k = [0,]
        self.l = [0,]
        self.m = [0,]
        self.n = [0,]
        self.o = [0,]
        self.p = [0,]
        self.out = [0,]
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
        self.gate15 = Not.Not()
    def _setup(self):
        self.gate0.a = self.a[0:1]
        self.gate0.b = self.a[1:2]
        self.b = self.gate0.outf()
        self.gate1.a = self.b
        self.gate1.b = self.a[2:3]
        self.c = self.gate1.outf()
        self.gate2.a = self.c
        self.gate2.b = self.a[3:4]
        self.d = self.gate2.outf()
        self.gate3.a = self.d
        self.gate3.b = self.a[4:5]
        self.e = self.gate3.outf()
        self.gate4.a = self.e
        self.gate4.b = self.a[5:6]
        self.f = self.gate4.outf()
        self.gate5.a = self.f
        self.gate5.b = self.a[6:7]
        self.g = self.gate5.outf()
        self.gate6.a = self.g
        self.gate6.b = self.a[7:8]
        self.h = self.gate6.outf()
        self.gate7.a = self.h
        self.gate7.b = self.a[8:9]
        self.i = self.gate7.outf()
        self.gate8.a = self.i
        self.gate8.b = self.a[9:10]
        self.j = self.gate8.outf()
        self.gate9.a = self.j
        self.gate9.b = self.a[10:11]
        self.k = self.gate9.outf()
        self.gate10.a = self.k
        self.gate10.b = self.a[11:12]
        self.l = self.gate10.outf()
        self.gate11.a = self.l
        self.gate11.b = self.a[12:13]
        self.m = self.gate11.outf()
        self.gate12.a = self.m
        self.gate12.b = self.a[13:14]
        self.n = self.gate12.outf()
        self.gate13.a = self.n
        self.gate13.b = self.a[14:15]
        self.o = self.gate13.outf()
        self.gate14.a = self.o
        self.gate14.b = self.a[15:16]
        self.p = self.gate14.outf()
        self.gate15.a = self.p
        self.out = self.gate15.outf()
    def outf(self):
        self._setup()
        return self.out
