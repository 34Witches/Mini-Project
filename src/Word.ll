[NAME]
Word

[INPUTS]
a, 16
load, 1

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Byte: a<a[0:8], load<load, out>out[0:8]
Byte: a<a[8:16], load<load, out>out[8:16]