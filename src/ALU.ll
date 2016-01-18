[NAME]
ALU

[INPUTS]
a, 16
b, 16
za, 1
na, 1
zb, 1
nb, 1
f, 1
no, 1

[OUTPUTS]
out, 16
zr, 1
ng, 1

[INTERNALS]
afterza, 16
nega, 16
fina, 16
afterzb, 16
negb, 16
finb, 16
anded, 16
added, 16
normalout, 16
negout, 16
test, 16

[LOGIC]
Mux16Bit: a<a, b<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], select<za, out>afterza
Not16Bit: a<afterza, out>nega
Mux16Bit: a<afterza, b<nega, select<na, out>fina
Mux16Bit: a<b, b<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], select<zb, out>afterzb
Not16Bit: a<afterzb, out>negb
Mux16Bit: a<afterzb, b<negb, select<nb, out>finb
And16Bit: a<fina, b<finb, out>anded
Adder16Bit: a<fina, b<finb, out>added
Mux16Bit: a<anded, b<added, select<f, out>normalout
Not16Bit: a<normalout, out>negout
Mux16Bit: a<normalout, b<negout, select<no, out>out, out>test, out[0:1]>ng
IsZero: a<test, out>zr
