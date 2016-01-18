[NAME]
PC

[INPUTS]
a, 15
inc, 1
load, 1
reset, 1

[OUTPUTS]
out, 15

[INTERNALS]
previous, 15
incremented, 15
maybeincremented, 15
maybeloaded, 15
final, 15

[LOGIC]
Adder16Bit: a[1:16]<previous, b<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], out[1:16]>incremented
Mux16Bit: a[1:16]<previous, b[1:16]<incremented, select<inc, out[1:16]>maybeincremented
Mux16Bit: a[1:16]<maybeincremented, b[1:16]<a, select<load, out[1:16]>maybeloaded
Mux16Bit: a[1:16]<maybeloaded, b<[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], select<reset, out[1:16]>final
Word: a[1:16]<final, load<[1], out[1:16]>out, out[1:16]>previous