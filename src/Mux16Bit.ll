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
Multiply: a<select, num<16, out>select16
Multiply: a<invselect, num<16, out>invselect16
And16Bit: a<a, b<invselect16, out>c
And16Bit: a<b, b<select16, out>d
Or16Bit: a<c, b<d, out>out