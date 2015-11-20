[NAME]
Adder

[INPUTS]
a, 1
b, 1
c, 1

[OUTPUTS]
out, 1
carry, 1

[INTERNALS]
d, 1
e, 1
f, 1

[LOGIC]
HalfAdder: a<a, b<b, out>d, carry>e
HalfAdder: a<c, b<d, out>out, carry>f
Or: a<e, b<f, out>carry