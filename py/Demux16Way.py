import Demux8Way
import Demux

class Demux16Way():
    def __init__(self):
        self.a = [0,]
        self.select = [0,0,0,0,]
        self.b = [0,]
        self.c = [0,]
        self.d = [0,]
        self.e = [0,]
        self.f = [0,]
        self.g = [0,]
        self.h = [0,]
        self.i = [0,]
        self.outa = [0,]
        self.outb = [0,]
        self.outc = [0,]
        self.outd = [0,]
        self.oute = [0,]
        self.outf = [0,]
        self.outg = [0,]
        self.outh = [0,]
        self.outi = [0,]
        self.outj = [0,]
        self.outk = [0,]
        self.outl = [0,]
        self.outm = [0,]
        self.outn = [0,]
        self.outo = [0,]
        self.outp = [0,]
        self.gate0 = Demux8Way.Demux8Way()
        self.gate1 = Demux.Demux()
        self.gate2 = Demux.Demux()
        self.gate3 = Demux.Demux()
        self.gate4 = Demux.Demux()
        self.gate5 = Demux.Demux()
        self.gate6 = Demux.Demux()
        self.gate7 = Demux.Demux()
        self.gate8 = Demux.Demux()
    def _setup(self):
        self.gate0.a = self.a
        self.gate0.select = self.select[0:3]
        self.b = self.gate0.outaf()
        self.c = self.gate0.outbf()
        self.d = self.gate0.outcf()
        self.e = self.gate0.outdf()
        self.f = self.gate0.outef()
        self.g = self.gate0.outff()
        self.h = self.gate0.outgf()
        self.i = self.gate0.outhf()
        self.gate1.a = self.b
        self.gate1.select = self.select[3:4]
        self.outa = self.gate1.outaf()
        self.outb = self.gate1.outbf()
        self.gate2.a = self.c
        self.gate2.select = self.select[3:4]
        self.outc = self.gate2.outaf()
        self.outd = self.gate2.outbf()
        self.gate3.a = self.d
        self.gate3.select = self.select[3:4]
        self.oute = self.gate3.outaf()
        self.outf = self.gate3.outbf()
        self.gate4.a = self.e
        self.gate4.select = self.select[3:4]
        self.outg = self.gate4.outaf()
        self.outh = self.gate4.outbf()
        self.gate5.a = self.f
        self.gate5.select = self.select[3:4]
        self.outi = self.gate5.outaf()
        self.outj = self.gate5.outbf()
        self.gate6.a = self.g
        self.gate6.select = self.select[3:4]
        self.outk = self.gate6.outaf()
        self.outl = self.gate6.outbf()
        self.gate7.a = self.h
        self.gate7.select = self.select[3:4]
        self.outm = self.gate7.outaf()
        self.outn = self.gate7.outbf()
        self.gate8.a = self.i
        self.gate8.select = self.select[3:4]
        self.outo = self.gate8.outaf()
        self.outp = self.gate8.outbf()
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
    def outif(self):
        self._setup()
        return self.outi
    def outjf(self):
        self._setup()
        return self.outj
    def outkf(self):
        self._setup()
        return self.outk
    def outlf(self):
        self._setup()
        return self.outl
    def outmf(self):
        self._setup()
        return self.outm
    def outnf(self):
        self._setup()
        return self.outn
    def outof(self):
        self._setup()
        return self.outo
    def outpf(self):
        self._setup()
        return self.outp
