import sys


def concatenate_sublists(metalist):
    return [item for sublist in metalist for item in sublist]


def uniquify(listin):
    elements = set()
    return [element for element in listin if not
            (element in elements or elements.add(element))]


def find_pin(pin):
    for gate in gates:
        for outpin in gate[2]:
            if outpin[1] == pin:
                return gates.index(gate)

readfile = open(sys.argv[1])
program = readfile.readlines()
program = [i.rstrip("\n") for i in program if (i != "\n") and (i[0] != "#")]
namepos = 0
inputspos = 0
outputspos = 0
logicpos = 0
internalpos = 0
lineno = 0
for line in program:
    if line == "[NAME]":
        namepos = lineno
    elif line == "[INPUTS]":
        inputspos = lineno
    elif line == "[OUTPUTS]":
        outputspos = lineno
    elif line == "[INTERNALS]":
        internalpos = lineno
    elif line == "[LOGIC]":
        logicpos = lineno
    lineno += 1

name = program[namepos+1]
writefile = open("../py/" + name + ".py", "w")
inputs = []
for i in program[inputspos+1:outputspos]:
    inputs.append(i.split(", "))

outputs = []
for i in program[outputspos+1:internalpos]:
    outputs.append(i.split(", "))

internals = []
for i in program[internalpos+1:logicpos]:
    internals.append(i.split(", "))

gatestemp = []
for i in program[logicpos+1:]:
    gatestemp.append(i.split(": "))

imports = [i for i in uniquify([i[0] for i in gatestemp])]
inpins = [i[0] for i in inputs]
outpins = [i[0] for i in outputs]
internalpins = [i[0] for i in internals]

gates = []
for gatetemp in gatestemp:
    gate = []
    gate.append(gatetemp[0])
    gatein = [j.split("<") for j in
              [i for i in gatetemp[1].split(", ") if "<" in i]]
    gate.append(gatein)
    gateout = [j.split(">") for j in
               [i for i in gatetemp[1].split(", ") if ">" in i]]
    gate.append(gateout)
    gates.append(gate)

for i in imports:
    writefile.write("import {0}\n".format(i))

writefile.write("\nclass {0}():\n    def __init__(self):\n".format(name))

for i in inputs:
    writefile.write("        self.{0} = [{1}]\n".format(i[0], int(i[1])*"0,"))

for i in internals:
    writefile.write("        self.{0} = [{1}]\n".format(i[0], int(i[1])*"0,"))

for i in outputs:
    writefile.write("        self.{0} = [{1}]\n".format(i[0], int(i[1])*"0,"))

for i in gates:
    writefile.write("        self.gate{0} = {1}.{1}()\n"
                    .format(gates.index(i), i[0]))

writefile.write("    def _setup(self):\n")

# for i in inpins + internalpins:
#     writefile.write("        self._{0} = self.{0}\n".format(i))

for gate in gates:
    gatenum = gates.index(gate)
    for pin in gate[1]:
        if pin[1][0] == '[':
            pinval = pin[1]
        else:
            pinval = "self." + pin[1]
        writefile.write("        self.gate{0}.{1} = {2}\n"
                        .format(gatenum, pin[0], pinval))
    for pin in gate[2]:
        if "[" in pin[0]:
            output = pin[0].split("[")
            output[1] = "[" + output[1]
        else:
            output = [pin[0], ""]
        writefile.write("        self.{0} = self.gate{1}.{2}f(){3}\n"
                        .format(pin[1], gatenum, output[0], output[1]))

for i in outputs:
    writefile.write("    def {0}f(self):\n"
                    "        self._setup()\n"
                    "        return self.{0}\n"
                    .format(i[0]))
