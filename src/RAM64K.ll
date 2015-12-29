[NAME]
RAM64K

[INPUTS]
a, 16
select, 16
load, 1

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Demux16Way: a<load, select<select[0:4], outa>b, outb>c, outc>d, outd>e, oute>f, outf>g, outg>h, outh>i, outi>j, outj>k, outk>l, outl>m, outm>n, outn>o, outo>p, outp>q
RAM4K: a<a, select<select[4:16], load<b, out>r
RAM4K: a<a, select<select[4:16], load<c, out>s
RAM4K: a<a, select<select[4:16], load<d, out>t
RAM4K: a<a, select<select[4:16], load<e, out>u
RAM4K: a<a, select<select[4:16], load<f, out>v
RAM4K: a<a, select<select[4:16], load<g, out>w
RAM4K: a<a, select<select[4:16], load<h, out>x
RAM4K: a<a, select<select[4:16], load<i, out>y
RAM4K: a<a, select<select[4:16], load<j, out>z
RAM4K: a<a, select<select[4:16], load<k, out>aa
RAM4K: a<a, select<select[4:16], load<l, out>ab
RAM4K: a<a, select<select[4:16], load<m, out>ac
RAM4K: a<a, select<select[4:16], load<n, out>ad
RAM4K: a<a, select<select[4:16], load<o, out>ae
RAM4K: a<a, select<select[4:16], load<p, out>af
RAM4K: a<a, select<select[4:16], load<q, out>ag
Mux16Bit16Way: a<r, b<s, c<t, d<u, e<v, f<w, g<x, h<y, i<z, j<aa, k<ab, l<ac, m<ad, n<ae, o<af, p<ag, select<select[0:4], out>out