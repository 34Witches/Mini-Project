[NAME]
Demux16Way

[INPUTS]
a, 1
select, 4

[OUTPUTS]
outa, 1
outb, 1
outc, 1
outd, 1
oute, 1
outf, 1
outg, 1
outh, 1
outi, 1
outj, 1
outk, 1
outl, 1
outm, 1
outn, 1
outo, 1
outp, 1

[INTERNALS]
b, 1
c, 1
d, 1
e, 1
f, 1
g, 1
h, 1
i, 1

[LOGIC]
Demux8Way: a<a, select<select[0:3], outa>b, outb>c, outc>d, outd>e, oute>f, outf>g, outg>h, outh>i
Demux: a<b, select<select[3:4], outa>outa, outb>outb
Demux: a<c, select<select[3:4], outa>outc, outb>outd
Demux: a<d, select<select[3:4], outa>oute, outb>outf
Demux: a<e, select<select[3:4], outa>outg, outb>outh
Demux: a<f, select<select[3:4], outa>outi, outb>outj
Demux: a<g, select<select[3:4], outa>outk, outb>outl
Demux: a<h, select<select[3:4], outa>outm, outb>outn
Demux: a<i, select<select[3:4], outa>outo, outb>outp
