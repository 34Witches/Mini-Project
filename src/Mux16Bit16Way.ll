[NAME]
Mux16Bit16Way

[INPUTS]
a, 16
b, 16
c, 16
d, 16
e, 16
f, 16
g, 16
h, 16
i, 16
j, 16
k, 16
l, 16
m, 16
n, 16
o, 16
p, 16
select, 4

[OUTPUTS]
out, 16

[INTERNALS]
q, 16
r, 16

[LOGIC]
Mux16Bit8Way: a<a, b<b, c<c, d<d, e<e, f<f, g<g, h<h, select<select[1:4], out>q
Mux16Bit8Way: a<i, b<j, c<k, d<l, e<m, f<n, g<o, h<p, select<select[1:4], out>r
Mux16Bit: a<q, b<r, select<select[0:1], out>out