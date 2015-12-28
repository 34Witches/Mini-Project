[NAME]
Demux

[INPUTS]
a, 1
select, 1

[OUTPUTS]
outa, 1
outb, 1

[INTERNALS]
invselect, 1

[LOGIC]
Not: a<select, out>invselect
And: a<a, b<invselect, out>outa
And: a<a, b<select, out>outb