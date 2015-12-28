[NAME]
Byte

[INPUTS]
a, 8
load, 1

[OUTPUTS]
out, 8

[INTERNALS]

[LOGIC]
Bit: a<a[0:1], load<load, out>out[0:1]
Bit: a<a[1:2], load<load, out>out[1:2]
Bit: a<a[2:3], load<load, out>out[2:3]
Bit: a<a[3:4], load<load, out>out[0:4]
Bit: a<a[4:5], load<load, out>out[4:5]
Bit: a<a[5:6], load<load, out>out[5:6]
Bit: a<a[6:7], load<load, out>out[6:7]
Bit: a<a[7:8], load<load, out>out[7:8]
