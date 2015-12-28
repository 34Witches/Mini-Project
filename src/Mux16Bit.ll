[NAME]
Mux16Bit

[INPUTS]
a, 16
b, 16
select, 1

[OUTPUTS]
out, 16

[INTERNALS]
invselect, 1
select16, 16
invselect16, 16
c, 16
d, 16

[LOGIC]
Not: a<select, out>invselect
And16Bit: a<a, b[0:1]<invselect, b[1:2]<invselect, b[2:3]<invselect, b[3:4]<invselect, b[4:5]<invselect, b[5:6]<invselect, b[6:7]<invselect, b[7:8]<invselect, b[8:9]<invselect, b[9:10]<invselect, b[10:11]<invselect, b[11:12]<invselect, b[12:13]<invselect, b[13:14]<invselect, b[14:15]<invselect, b[15:16]<invselect, out>c
And16Bit: a<b, b[0:1]<select, b[1:2]<select, b[2:3]<select, b[3:4]<select, b[4:5]<select, b[5:6]<select, b[6:7]<select, b[7:8]<select, b[8:9]<select, b[9:10]<select, b[10:11]<select, b[11:12]<select, b[12:13]<select, b[13:14]<select, b[14:15]<select, b[15:16]<select, out>d
Or16Bit: a<c, b<d, out>out