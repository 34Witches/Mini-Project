[NAME]
Mux16Bit

[INPUTS]
a, 16
b, 16
select, 1

[OUTPUTS]
out, 16

[INTERNALS]
invselect, 1
select16, 16
invselect16, 16
c, 16
d, 16

[LOGIC]
Not: a<select, out>invselect
And16Bit: a<a, b<(invselect*16), out>c
And16Bit: a<b, b<(select*16), out>d
Or16Bit: a<c, b<d, out>out