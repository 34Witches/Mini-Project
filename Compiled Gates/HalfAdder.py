import Xor
import And

class HalfAdder():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]
        self.out = [0,]
        self.carry = [0,]
        self.gate0 = Xor.Xor()
        self.gate1 = And.And()
    def _setup(self):
        self._a = self.a
        self._b = self.b
        self.gate0.a = self._a
        self.gate0.b = self._b
        self.out = self.gate0.outf()
        self.gate1.a = self._a
        self.gate1.b = self._b
        self.carry = self.gate1.outf()
    def outf(self):
        self._setup()
        return self.out
    def carryf(self):
        self._setup()
        return self.carry
