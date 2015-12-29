[NAME]
RAM16

[INPUTS]
a, 16
select, 4
load, 1

[OUTPUTS]
out, 16

[INTERNALS]
b, 1
c, 1
d, 1
e, 1
f, 1
g, 1
h, 1
i, 1
j, 1
k, 1
l, 1
m, 1
n, 1
o, 1
p, 1
q, 1
r, 16
s, 16
t, 16
u, 16
v, 16
w, 16
x, 16
y, 16
z, 16
aa, 16
ab, 16
ac, 16
ad, 16
ae, 16
af, 16
ag, 16

[LOGIC]
Demux16Way: a<load, select<select, outa>b, outb>c, outc>d, outd>e, oute>f, outf>g, outg>h, outh>i, outi>j, outj>k, outk>l, outl>m, outm>n, outn>o, outo>p, outp>q
Word: a<a, load<b, out>r
Word: a<a, load<c, out>s
Word: a<a, load<d, out>t
Word: a<a, load<e, out>u
Word: a<a, load<f, out>v
Word: a<a, load<g, out>w
Word: a<a, load<h, out>x
Word: a<a, load<i, out>y
Word: a<a, load<j, out>z
Word: a<a, load<k, out>aa
Word: a<a, load<l, out>ab
Word: a<a, load<m, out>ac
Word: a<a, load<n, out>ad
Word: a<a, load<o, out>ae
Word: a<a, load<p, out>af
Word: a<a, load<q, out>ag
Mux16Bit16Way: a<r, b<s, c<t, d<u, e<v, f<w, g<x, h<y, i<z, j<aa, k<ab, l<ac, m<ad, n<ae, o<af, p<ag, select<select, out>out