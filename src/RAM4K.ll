[NAME]
RAM4K

[INPUTS]
a, 16
select, 12
load, 1

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Demux16Way: a<load, select<select[0:4], outa>b, outb>c, outc>d, outd>e, oute>f, outf>g, outg>h, outh>i, outi>j, outj>k, outk>l, outl>m, outm>n, outn>o, outo>p, outp>q
RAM256: a<a, select<select[4:12], load<b, out>r
RAM256: a<a, select<select[4:12], load<c, out>s
RAM256: a<a, select<select[4:12], load<d, out>t
RAM256: a<a, select<select[4:12], load<e, out>u
RAM256: a<a, select<select[4:12], load<f, out>v
RAM256: a<a, select<select[4:12], load<g, out>w
RAM256: a<a, select<select[4:12], load<h, out>x
RAM256: a<a, select<select[4:12], load<i, out>y
RAM256: a<a, select<select[4:12], load<j, out>z
RAM256: a<a, select<select[4:12], load<k, out>aa
RAM256: a<a, select<select[4:12], load<l, out>ab
RAM256: a<a, select<select[4:12], load<m, out>ac
RAM256: a<a, select<select[4:12], load<n, out>ad
RAM256: a<a, select<select[4:12], load<o, out>ae
RAM256: a<a, select<select[4:12], load<p, out>af
RAM256: a<a, select<select[4:12], load<q, out>ag
Mux16Bit16Way: a<r, b<s, c<t, d<u, e<v, f<w, g<x, h<y, i<z, j<aa, k<ab, l<ac, m<ad, n<ae, o<af, p<ag, select<select[0:4], out>out