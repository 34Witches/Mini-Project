import Mux16Bit
import Not16Bit
import And16Bit
import Adder16Bit
import IsZero

class ALU():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.za = [0,]
        self.na = [0,]
        self.zb = [0,]
        self.nb = [0,]
        self.f = [0,]
        self.no = [0,]
        self.afterza = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.nega = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.fina = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.afterzb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.negb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.finb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.and = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.add = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.normalout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.negout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.zr = [0,]
        self.ng = [0,]
        self.gate0 = Mux16Bit.Mux16Bit()
        self.gate1 = Not16Bit.Not16Bit()
        self.gate2 = Mux16Bit.Mux16Bit()
        self.gate3 = Mux16Bit.Mux16Bit()
        self.gate4 = Not16Bit.Not16Bit()
        self.gate5 = Mux16Bit.Mux16Bit()
        self.gate6 = And16Bit.And16Bit()
        self.gate7 = Adder16Bit.Adder16Bit()
        self.gate8 = Mux16Bit.Mux16Bit()
        self.gate9 = Not16Bit.Not16Bit()
        self.gate10 = Mux16Bit.Mux16Bit()
        self.gate11 = IsZero.IsZero()
    def _setup(self):
        self.gate0.a = self.a
        self.gate0.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gate0.select = self.za
        self.afterza = self.gate0.outf()
        self.gate1.a = self.afterza
        self.nega = self.gate1.outf()
        self.gate2.a = self.afterza
        self.gate2.b = self.nega
        self.gate2.selext = self.na
        self.fina = self.gate2.outf()
        self.gate3.a = self.b
        self.gate3.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gate3.select = self.zb
        self.afterzb = self.gate3.outf()
        self.gate4.a = self.afterzb
        self.negb = self.gate4.outf()
        self.gate5.a = self.afterzb
        self.gate5.b = self.negb
        self.gate5.selext = self.nb
        self.finb = self.gate5.outf()
        self.gate6.a = self.fina
        self.gate6.b = self.finb
        self.and = self.gate6.outf()
        self.gate7.a = self.fina
        self.gate7.b = self.finb
        self.add = self.gate7.outf()
        self.gate8.a = self.and
        self.gate8.b = self.add
        self.gate8.select = self.f
        self.normalout = self.gate8.outf()
        self.gate9.a = self.normalout
        self.negout = self.gate9.outf()
        self.gate10.a = self.normalout
        self.gate10.b = self.negout
        self.gate10.select = self.no
        self.out = self.gate10.outf()
        self.test = self.gate10.outf()
        self.ng = self.gate10.outf()[0:1]
        self.gate11.a = self.test
        self.zr = self.gate11.outf()
    def outf(self):
        self._setup()
        return self.out
    def zrf(self):
        self._setup()
        return self.zr
    def ngf(self):
        self._setup()
        return self.ng
