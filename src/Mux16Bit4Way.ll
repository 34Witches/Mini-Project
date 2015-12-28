[NAME]
Mux16Bit4Way

[INPUTS]
a, 16
b, 16
c, 16
d, 16
select, 2

[OUTPUTS]
out, 16

[INTERNALS]
e, 16
f, 16

[LOGIC]
Mux16Bit: a<a, b<b, select<select[1:2], out>e
Mux16Bit: a<c, b<d, select<select[1:2], out>f
Mux16Bit: a<e, b<f, select<select[0:1], out>out