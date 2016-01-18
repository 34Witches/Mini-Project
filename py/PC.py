import Adder16Bit
import Mux16Bit
import Word

class PC():
    def __init__(self):
        self.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.inc = [0,]
        self.load = [0,]
        self.reset = [0,]
        self.previous = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.incremented = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.maybeincremented = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.maybeloaded = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.final = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Adder16Bit.Adder16Bit()
        self.gate1 = Mux16Bit.Mux16Bit()
        self.gate2 = Mux16Bit.Mux16Bit()
        self.gate3 = Mux16Bit.Mux16Bit()
        self.gate4 = Word.Word()
    def _setup(self):
        self.gate0.a[1:16] = self.previous
        self.gate0.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        self.incremented = self.gate0.outf()[1:16]
        self.gate1.a[1:16] = self.previous
        self.gate1.b[1:16] = self.incremented
        self.gate1.select = self.inc
        self.maybeincremented = self.gate1.outf()[1:16]
        self.gate2.a[1:16] = self.maybeincremented
        self.gate2.b[1:16] = self.a
        self.gate2.select = self.load
        self.maybeloaded = self.gate2.outf()[1:16]
        self.gate3.a[1:16] = self.maybeloaded
        self.gate3.b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gate3.select = self.reset
        self.final = self.gate3.outf()[1:16]
        self.gate4.a[1:16] = self.final
        self.gate4.load = [1]
        self.out = self.gate4.outf()[1:16]
        self.previous = self.gate4.outf()[1:16]
    def outf(self):
        self._setup()
        return self.out
