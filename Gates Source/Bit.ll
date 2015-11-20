[NAME]
Bit

[INPUTS]
a, 1
load, 1

[OUTPUTS]
out, 1

[INTERNALS]

[LOGIC]
Mux: a<c, b<a, select<load, out>b
DFF: a<b, out>c