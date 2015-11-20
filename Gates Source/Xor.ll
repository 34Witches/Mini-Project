[NAME]
Xor

[INPUTS]
a, 1
b, 1

[OUTPUTS]
out, 1

[INTERNALS]
c, 1
d, 1

[LOGIC]
Or: a<a, b<b, out>c
Nand: a<a, b<b, out>d
And: a<c, b<d, out>out