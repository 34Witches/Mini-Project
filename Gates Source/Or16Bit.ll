[NAME]
Or16Bit

[INPUTS]
a, 16
b, 16

[OUTPUTS]
out, 16

[INTERNALS]

[LOGIC]
Or: a<a[0:1], b<b[0:1], out>out[0:1]
Or: a<a[1:2], b<b[1:2], out>out[1:2]
Or: a<a[2:3], b<b[2:3], out>out[2:3]
Or: a<a[3:4], b<b[3:4], out>out[3:4]
Or: a<a[4:5], b<b[4:5], out>out[4:5]
Or: a<a[5:6], b<b[5:6], out>out[5:6]
Or: a<a[6:7], b<b[6:7], out>out[6:7]
Or: a<a[7:8], b<b[7:8], out>out[7:8]
Or: a<a[8:9], b<b[8:9], out>out[8:9]
Or: a<a[9:10], b<b[9:10], out>out[9:10]
Or: a<a[10:11], b<b[10:11], out>out[10:11]
Or: a<a[11:12], b<b[11:12], out>out[11:12]
Or: a<a[12:13], b<b[12:13], out>out[12:13]
Or: a<a[13:14], b<b[13:14], out>out[13:14]
Or: a<a[14:15], b<b[14:15], out>out[14:15]
Or: a<a[15:], b<b[15:], out>out[15:]
