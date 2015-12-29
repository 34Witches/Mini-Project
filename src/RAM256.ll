[NAME]
RAM256

[INPUTS]
a, 16
select, 8
load, 1

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Demux16Way: a<load, select<select[0:4], outa>b, outb>c, outc>d, outd>e, oute>f, outf>g, outg>h, outh>i, outi>j, outj>k, outk>l, outl>m, outm>n, outn>o, outo>p, outp>q
RAM16: a<a, select<select[4:8], load<b, out>r
RAM16: a<a, select<select[4:8], load<c, out>s
RAM16: a<a, select<select[4:8], load<d, out>t
RAM16: a<a, select<select[4:8], load<e, out>u
RAM16: a<a, select<select[4:8], load<f, out>v
RAM16: a<a, select<select[4:8], load<g, out>w
RAM16: a<a, select<select[4:8], load<h, out>x
RAM16: a<a, select<select[4:8], load<i, out>y
RAM16: a<a, select<select[4:8], load<j, out>z
RAM16: a<a, select<select[4:8], load<k, out>aa
RAM16: a<a, select<select[4:8], load<l, out>ab
RAM16: a<a, select<select[4:8], load<m, out>ac
RAM16: a<a, select<select[4:8], load<n, out>ad
RAM16: a<a, select<select[4:8], load<o, out>ae
RAM16: a<a, select<select[4:8], load<p, out>af
RAM16: a<a, select<select[4:8], load<q, out>ag
Mux16Bit16Way: a<r, b<s, c<t, d<u, e<v, f<w, g<x, h<y, i<z, j<aa, k<ab, l<ac, m<ad, n<ae, o<af, p<ag, select<select[0:4], out>out