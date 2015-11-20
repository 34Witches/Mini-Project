class Nand():
    def __init__(self):
        self.a = [0,]
        self.b = [0,]

    def outf(self):
        return {((0,),(0,)):[1,],((1,),(0,)):[1,],((0,),(1,)):[1,],((1,),(1,)):[0,]}[(tuple(self.a),tuple(self.b))]
