[NAME]
Demux8Way

[INPUTS]
a, 1
select, 3

[OUTPUTS]
outa, 1
outb, 1
outc, 1
outd, 1
oute, 1
outf, 1
outg, 1
outh, 1

[INTERNALS]
b, 1
c, 1
d, 1
e, 1

[LOGIC]
Demux4Way: a<a, select<select[0:2], outa>b, outb>c, outc>d, outd>e
Demux: a<b, select<select[2:3], outa>outa, outb>outb
Demux: a<c, select<select[2:3], outa>outc, outb>outd
Demux: a<d, select<select[2:3], outa>oute, outb>outf
Demux: a<e, select<select[2:3], outa>outg, outb>outh
