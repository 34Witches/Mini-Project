[NAME]
Demux4Way

[INPUTS]
a, 1
select, 2

[OUTPUTS]
outa, 1
outb, 1
outc, 1
outd, 1

[INTERNALS]
b, 1
c, 1

[LOGIC]
Demux: a<a, select<select[0:1], outa>b, outb>c
Demux: a<b, select<select[1:2], outa>outa, outb>outb
Demux: a<c, select<select[1:2], outa>outc, outb>outd