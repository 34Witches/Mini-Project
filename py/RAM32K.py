import Demux8Way
import RAM4K
import Mux16Bit8Way

class RAM32K():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.select = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.load = [0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Demux8Way.Demux8Way()
        self.gate1 = RAM4K.RAM4K()
        self.gate2 = RAM4K.RAM4K()
        self.gate3 = RAM4K.RAM4K()
        self.gate4 = RAM4K.RAM4K()
        self.gate5 = RAM4K.RAM4K()
        self.gate6 = RAM4K.RAM4K()
        self.gate7 = RAM4K.RAM4K()
        self.gate8 = RAM4K.RAM4K()
        self.gate9 = Mux16Bit8Way.Mux16Bit8Way()
    def _setup(self):
        self.gate0.a = self.load
        self.gate0.select = self.select[0:3]
        self.b = self.gate0.outaf()
        self.c = self.gate0.outbf()
        self.d = self.gate0.outcf()
        self.e = self.gate0.outdf()
        self.f = self.gate0.outef()
        self.g = self.gate0.outff()
        self.h = self.gate0.outgf()
        self.i = self.gate0.outhf()
        self.gate1.a = self.a
        self.gate1.select = self.select[3:15]
        self.gate1.load = self.b
        self.r = self.gate1.outf()
        self.gate2.a = self.a
        self.gate2.select = self.select[3:15]
        self.gate2.load = self.cy out>s
        self.s = self.gate2.load<cy outf()
        self.gate3.a = self.a
        self.gate3.select = self.select[3:15]
        self.gate3.load = self.d
        self.t = self.gate3.outf()
        self.gate4.a = self.a
        self.gate4.select = self.select[3:15]
        self.gate4.load = self.e
        self.u = self.gate4.outf()
        self.gate5.a = self.a
        self.gate5.select = self.select[3:15]
        self.gate5.load = self.f
        self.v = self.gate5.outf()
        self.gate6.a = self.a
        self.gate6.select = self.select[3:15]
        self.gate6.load = self.g
        self.w = self.gate6.outf()
        self.gate7.a = self.a
        self.gate7.select = self.select[3:15]
        self.gate7.load = self.h
        self.x = self.gate7.outf()
        self.gate8.a = self.a
        self.gate8.select = self.select[3:15]
        self.gate8.load = self.i
        self.y = self.gate8.outf()
        self.gate9.a = self.r
        self.gate9.b = self.s
        self.gate9.c = self.t
        self.gate9.d = self.u
        self.gate9.e = self.v
        self.gate9.f = self.w
        self.gate9.g = self.x
        self.gate9.h = self.y
        self.gate9.select = self.select[0:3]
        self.out = self.gate9.outf()
    def outf(self):
        self._setup()
        return self.out
