import Not
import And

class Demux():
    def __init__(self):
        self.a = [0,]
        self.select = [0,]
        self.invselect = [0,]
        self.outa = [0,]
        self.outb = [0,]
        self.gate0 = Not.Not()
        self.gate1 = And.And()
        self.gate2 = And.And()
    def _setup(self):
        self._a = self.a
        self._select = self.select
        self._invselect = self.invselect
        self.gate0.a = self._select
        self.invselect = self.gate0.outf()
        self.gate1.a = self._a
        self.gate1.b = self._invselect
        self.outa = self.gate1.outf()
        self.gate2.a = self._a
        self.gate2.b = self._select
        self.outb = self.gate2.outf()
    def outaf(self):
        self._setup()
        return self.outa
    def outbf(self):
        self._setup()
        return self.outb
