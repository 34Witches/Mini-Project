[NAME]
And

[INPUTS]
a, 1
b, 1

[OUTPUTS]
out, 1

[INTERNALS]
c, 1

[LOGIC]
Nand: a<a, b<b, out>c
Not: a<c, out>out
