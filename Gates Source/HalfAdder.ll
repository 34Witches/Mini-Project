[NAME]
HalfAdder

[INPUTS]
a, 1
b, 1

[OUTPUTS]
out, 1
carry, 1

[INTERNALS]

[LOGIC]
Xor: a<a, b<b, out>out
And: a<a, b<b, out>carry