import Demux4Way
import Demux

class Demux8Way():
    def __init__(self):
        self.a = [0,]
        self.select = [0,0,0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.e = [0,]
        self.outa = [0,]
        self.outb = [0,]
        self.outc = [0,]
        self.outd = [0,]
        self.oute = [0,]
        self.outf = [0,]
        self.outg = [0,]
        self.outh = [0,]
        self.gate0 = Demux4Way.Demux4Way()
        self.gate1 = Demux.Demux()
        self.gate2 = Demux.Demux()
        self.gate3 = Demux.Demux()
        self.gate4 = Demux.Demux()
    def _setup(self):
        self.gate0.a = self.a
        self.gate0.select = self.select[0:2]
        self.b = self.gate0.outaf()
        self.c = self.gate0.outbf()
        self.d = self.gate0.outcf()
        self.e = self.gate0.outdf()
        self.gate1.a = self.b
        self.gate1.select = self.select[2:3]
        self.outa = self.gate1.outaf()
        self.outb = self.gate1.outbf()
        self.gate2.a = self.c
        self.gate2.select = self.select[2:3]
        self.outc = self.gate2.outaf()
        self.outd = self.gate2.outbf()
        self.gate3.a = self.d
        self.gate3.select = self.select[2:3]
        self.oute = self.gate3.outaf()
        self.outf = self.gate3.outbf()
        self.gate4.a = self.e
        self.gate4.select = self.select[2:3]
        self.outg = self.gate4.outaf()
        self.outh = self.gate4.outbf()
    def outaf(self):
        self._setup()
        return self.outa
    def outbf(self):
        self._setup()
        return self.outb
    def outcf(self):
        self._setup()
        return self.outc
    def outdf(self):
        self._setup()
        return self.outd
    def outef(self):
        self._setup()
        return self.oute
    def outff(self):
        self._setup()
        return self.outf
    def outgf(self):
        self._setup()
        return self.outg
    def outhf(self):
        self._setup()
        return self.outh
