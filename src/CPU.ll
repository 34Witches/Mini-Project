[NAME]
CPU

[INPUTS]
memory, 16
instruction, 16
reset, 1

[OUTPUTS]
out, 16
towrite, 1
address, 15
counter, 15

[INTERNALS]
ina, 16
writea, 1
vala, 16
inb, 16
writeb, 1
valb, 16
instructioncode, 16
alua, 16
alub, 16
aluout, 16
iszero, 1
isnegative, 1
null, 1
writea1, 1
writea2, 1


[LOGIC]
#A Register
Word: a<ina, load<writea, out>vala, out[1:16]>address

#B Register
Word: a<inb, load<writeb, out>valb

Mux16Bit: a<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], b<instruction, select<instruction[0:1], out>instructioncode

Mux16Bit4Way: a<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], b<vala, c<valb, d<memory, select<instructioncode[1:3], out>alua
Mux16Bit4Way: a<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], b<vala, c<valb, d<memory, select<instructioncode[3:5], out>alub

ALU: a<alua, b<alub, za<instructioncode[7:8], na<instructioncode[8:9], zb<instructioncode[9:10], nb<instructioncode[10:11], f<instructioncode[11:12], no<instructioncode[12:13], out>aluout, out>inb, out>out, zr>iszero, ng>isnegative

Mux16Bit: a<instruction, b<aluout, select<instruction[0:1], out>ina

Demux4Way: a<[1], select<instructioncode[5:7], outa>null, outb>writea1, outc>writeb, outd>towrite
Not: a<instruction[0:1], out>writea2
Or: a<writea1, b<writea2, out>writea

Mux4Way: a<[0], b<iszero, c<isnegative, d<[1], select<instructioncode[13:15], out>toload

PC: a<vala[1:16], inc<[1], load<toload, reset<reset, out>counter
