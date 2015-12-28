import Demux

class Demux4Way():
    def __init__(self):
        self.a = [0,]
        self.select = [0,0,]
        self.b = [0,]
        self.c = [0,]
        self.outa = [0,]
        self.outb = [0,]
        self.outc = [0,]
        self.outd = [0,]
        self.gate0 = Demux.Demux()
        self.gate1 = Demux.Demux()
        self.gate2 = Demux.Demux()
    def _setup(self):
        self._a = self.a
        self._select = self.select
        self._b = self.b
        self._c = self.c
        self.gate0.a = self._a
        self.gate0.select = self._select[0:1]
        self.b = self.gate0.outaf()
        self.c = self.gate0.outbf()
        self.gate1.a = self._b
        self.gate1.select = self._select[1:2]
        self.outa = self.gate1.outaf()
        self.outb = self.gate1.outbf()
        self.gate2.a = self._c
        self.gate2.select = self._select[1:2]
        self.outc = self.gate2.outaf()
        self.outd = self.gate2.outbf()
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
