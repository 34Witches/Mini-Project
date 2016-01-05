import Word
import Mux16Bit
import Mux16Bit4Way
import ALU
import Demux4Way
import Not
import Or
import Mux4Way
import PC

class CPU():
    def __init__(self):
        self.memory = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.instruction = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.reset = [0,]
        self.ina = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.writea = [0,]
        self.vala = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.inb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.writeb = [0,]
        self.valb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.instructioncode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.alua = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.alub = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.aluout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.iszero = [0,]
        self.isnegative = [0,]
        self.null = [0,]
        self.writea1 = [0,]
        self.writea2 = [0,]
        self.out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.towrite = [0,]
        self.address = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
        self.gate0 = Word.Word()
        self.gate1 = Word.Word()
        self.gate2 = Mux16Bit.Mux16Bit()
        self.gate3 = Mux16Bit4Way.Mux16Bit4Way()
        self.gate4 = Mux16Bit4Way.Mux16Bit4Way()
        self.gate5 = ALU.ALU()
        self.gate6 = Mux16Bit.Mux16Bit()
        self.gate7 = Demux4Way.Demux4Way()
        self.gate8 = Not.Not()
        self.gate9 = Or.Or()
        self.gate10 = Mux4Way.Mux4Way()
        self.gate11 = PC.PC()
    def _setup(self):
        self.gate0.a = self.ina
        self.gate0.load = self.writea
        self.vala = self.gate0.outf()
        self.address = self.gate0.outf()[1:16]
        self.gate1.a = self.inb
        self.gate1.load = self.writeb
        self.valb = self.gate1.outf()
        self.gate2.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gate2.b = self.instruction
        self.gate2.select = self.instruction[0:1]
        self.instructioncode = self.gate2.outf()
        self.gate3.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gate3.b = self.vala
        self.gate3.c = self.valb
        self.gate3.d = self.memory
        self.gate3.select = self.instructioncode[1:3]
        self.alua = self.gate3.outf()
        self.gate4.a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.gate4.b = self.vala
        self.gate4.c = self.valb
        self.gate4.d = self.memory
        self.gate4.select = self.instructioncode[3:5]
        self.alub = self.gate4.outf()
        self.gate5.a = self.alua
        self.gate5.b = self.alub
        self.gate5.za = self.instructioncode[7:8]
        self.gate5.na = self.instructioncode[8:9]
        self.gate5.zb = self.instructioncode[9:10]
        self.gate5.nb = self.instructioncode[10:11]
        self.gate5.f = self.instructioncode[11:12]
        self.gate5.no = self.instructioncode[12:13]
        self.aluout = self.gate5.outf()
        self.inb = self.gate5.outf()
        self.out = self.gate5.outf()
        self.iszero = self.gate5.zrf()
        self.isnegative = self.gate5.ngf()
        self.gate6.a = self.instruction
        self.gate6.b = self.aluout
        self.gate6.select = self.instruction[0:1]
        self.ina = self.gate6.outf()
        self.gate7.a = [1]
        self.gate7.select = self.instructioncode[5:7]
        self.null = self.gate7.outaf()
        self.writea1 = self.gate7.outbf()
        self.writeb = self.gate7.outcf()
        self.towrite = self.gate7.outdf()
        self.gate8.a = self.instruction[0:1]
        self.writea2 = self.gate8.outf()
        self.gate9.a = self.writea1
        self.gate9.b = self.writea2
        self.writea = self.gate9.outf()
        self.gate10.a = [0]
        self.gate10.b = self.iszero
        self.gate10.c = self.isnegative
        self.gate10.d = [1]
        self.gate10.select = self.instructioncode[13:15]
        self.toload = self.gate10.outf()
        self.gate11.a = self.vala[1:16]
        self.gate11.inc = [1]
        self.gate11.load = self.toload
        self.gate11.reset = self.reset
        self.counter = self.gate11.outf()
    def outf(self):
        self._setup()
        return self.out
    def towritef(self):
        self._setup()
        return self.towrite
    def addressf(self):
        self._setup()
        return self.address
    def counterf(self):
        self._setup()
        return self.counter
