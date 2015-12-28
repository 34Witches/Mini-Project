[NAME]
Mux16Bit8Way

[INPUTS]
a, 16
b, 16
c, 16
d, 16
e, 16
f, 16
g, 16
h, 16
select, 3

[OUTPUTS]
out, 16

[INTERNALS]
i, 16
j, 16

[LOGIC]
Mux16Bit4Way: a<a, b<b, c<c, d<d, select<select[1:3], out>i
Mux16Bit4Way: a<e, b<f, c<g, d<h, select<select[1:3], out>j
Mux16Bit: a<i, b<j, select<select[0:1], out>out