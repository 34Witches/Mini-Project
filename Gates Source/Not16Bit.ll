[NAME]
Not16Bit

[INPUTS]
a, 16

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Not: a<a[0:1], out>out[0:1]
Not: a<a[1:2], out>out[1:2]
Not: a<a[2:3], out>out[2:3]
Not: a<a[3:4], out>out[3:4]
Not: a<a[4:5], out>out[4:5]
Not: a<a[5:6], out>out[5:6]
Not: a<a[6:7], out>out[6:7]
Not: a<a[7:8], out>out[7:8]
Not: a<a[8:9], out>out[8:9]
Not: a<a[9:10], out>out[9:10]
Not: a<a[10:11], out>out[10:11]
Not: a<a[11:12], out>out[11:12]
Not: a<a[12:13], out>out[12:13]
Not: a<a[13:14], out>out[13:14]
Not: a<a[14:15], out>out[14:15]
Not: a<a[15:], out>out[15:]
