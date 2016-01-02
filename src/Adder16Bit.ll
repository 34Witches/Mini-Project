[NAME]
Adder16Bit

[INPUTS]
a, 16
b, 16

[OUTPUTS]
out, 16

[INTERNALS]
c1, 1
c2, 1
c3, 1
c4, 1
c5, 1
c6, 1
c7, 1
c8, 1
c9, 1
c10, 1
c11, 1
c12, 1
c13, 1
c14, 1
c15, 1

[LOGIC]
HalfAdder: a<a[0:1], b<b[0:1], out>out[0:1], carry>c1
Adder: a<a[1:2], b<b[1:2], c<c1, out>out[1:2], carry>c2
Adder: a<a[2:3], b<b[2:3], c<c2, out>out[2:3], carry>c3
Adder: a<a[3:4], b<b[3:4], c<c3, out>out[3:4], carry>c4
Adder: a<a[4:5], b<b[4:5], c<c4, out>out[4:5], carry>c5
Adder: a<a[5:6], b<b[5:6], c<c5, out>out[5:6], carry>c6
Adder: a<a[6:7], b<b[6:7], c<c6, out>out[6:7], carry>c7
Adder: a<a[7:8], b<b[7:8], c<c7, out>out[7:8], carry>c8
Adder: a<a[8:9], b<b[8:9], c<c8, out>out[8:9], carry>c9
Adder: a<a[9:10], b<b[9:10], c<c9, out>out[9:10], carry>c10
Adder: a<a[10:11], b<b[10:11], c<c10, out>out[10:11], carry>c11
Adder: a<a[11:12], b<b[11:12], c<c11, out>out[11:12], carry>c12
Adder: a<a[12:13], b<b[12:13], c<c12, out>out[12:13], carry>c13
Adder: a<a[13:14], b<b[13:14], c<c13, out>out[13:14], carry>c14
Adder: a<a[14:15], b<b[14:15], c<c14, out>out[14:15], carry>c15
AdderEnd: a<a[15:16], b<b[15:16], c<c15, out>out[15:16]
