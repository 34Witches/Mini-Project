[NAME]
IsZero

[INPUTS]
a, 16

[OUTPUTS]
out, 1

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

[LOGIC]
Or: a<a[0:1], b<a[1:2], out>b
Or: a<b, b<a[2:3], out>c
Or: a<c, b<a[3:4], out>d
Or: a<d, b<a[4:5], out>e
Or: a<e, b<a[5:6], out>f
Or: a<f, b<a[6:7], out>g
Or: a<g, b<a[7:8], out>h
Or: a<h, b<a[8:9], out>i
Or: a<i, b<a[9:10], out>j
Or: a<j, b<a[10:11], out>k
Or: a<k, b<a[11:12], out>l
Or: a<l, b<a[12:13], out>m
Or: a<m, b<a[13:14], out>n
Or: a<n, b<a[14:15], out>o
Or: a<o, b<a[15:16], out>p
Not: a<p, out>out
