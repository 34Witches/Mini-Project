[NAME]
Mux4Way

[INPUTS]
a, 1
b, 1
c, 1
d, 1
select, 2

[OUTPUTS]
out, 1

[INTERNALS]

[LOGIC]
Mux: a<a, b<b, select<select[1:2], out>e
Mux: a<c, b<d, select<select[1:2], out>f
Mux: a<e, b<f, select<select[0:1], out>out