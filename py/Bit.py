class Bit():

    bits = []

    def __init__(self):
        type(self).bits.append(self)
        self.a = [0]
        self.load = [0]
        self.out = [0]

    @classmethod
    def tick(cls):
        for i in cls.bits:
            i.update()

    def update(self):
        if self.load[0]:
            self.out = self.a

    def outf(self):
        return self.out