[NAME]
AdderEnd

[INPUTS]
a, 1
b, 1
c, 1

[OUTPUTS]
out, 1

[INTERNALS]
d, 1

[LOGIC]
Xor: a<a, b<b, out>d
Xor: a<c, b<d, out>out