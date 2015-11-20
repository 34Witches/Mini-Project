[NAME]
Or

[INPUTS]
a, 1
b, 1

[OUTPUTS]
out, 1

[INTERNALS]
c, 1
d, 1

[LOGIC]
Not: a<a, out>c
Not: a<b, out>d
Nand: a<c, b<d, out>out