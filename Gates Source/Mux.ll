[NAME]
Mux

[INPUTS]
a, 1
b, 1
select, 1

[OUTPUTS]
out, 1

[INTERNALS]
c, 1
d, 1
invselect, 1

[LOGIC]
Not: a<select, out>invselect
And: a<a, b<invselect, out>c
And: a<b, b<select, out>d
Or: a<c, b<d, out>out