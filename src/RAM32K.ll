[NAME]
RAM32K

[INPUTS]
a, 16
select, 15
load, 1

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Demux8Way: a<load, select<select[0:3], outa>b, outb>c, outc>d, outd>e, oute>f, outf>g, outg>h, outh>i
RAM4K: a<a, select<select[3:15], load<b, out>r
RAM4K: a<a, select<select[3:15], load<cy out>s
RAM4K: a<a, select<select[3:15], load<d, out>t
RAM4K: a<a, select<select[3:15], load<e, out>u
RAM4K: a<a, select<select[3:15], load<f, out>v
RAM4K: a<a, select<select[3:15], load<g, out>w
RAM4K: a<a, select<select[3:15], load<h, out>x
RAM4K: a<a, select<select[3:15], load<i, out>y
Mux16Bit8Way: a<r, b<s, c<t, d<u, e<v, f<w, g<x, h<y, select<select[0:3], out>out
