###########################################################################
# import

import re

###########################################################################
# constants

input1 = "input_d10_tst.txt"
input2 = "input_d10.txt"
max_val = 65536
max_steps = 5000000

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def convert_lines_to_program(lines):
	prglines = []
	labels = {}
	for l in lines:
		if "ba" in l:
			l2 = l.split("ba")
			l3 = l2[1].split("ne")
			l4 = []
			for i in range(len(l3)):
				l4.append(len(re.findall("na", l3[i])))
			match l4[0]:
				#0 nas: Load immediate value into register. (val, dest_reg)
				case 0:
					prglines.append(["load", l4[1], l4[2]])
				#1 na: Copy value from one register to another. (src_reg, dest_reg)
				case 1:
					prglines.append(["copy", l4[1], l4[2]])
				#2 nas: Add values from two registers and store result in a third register. (src_reg1, src_reg2, dest_reg)
				case 2:
					prglines.append(["add", l4[1], l4[2], l4[3]])
				#3 nas: Subtract values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
				case 3:
					prglines.append(["sub", l4[1], l4[2], l4[3]])
				#4 nas: Multiply values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
				case 4:
					prglines.append(["mult", l4[1], l4[2], l4[3]])
				#5 nas: Modulo values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
				case 5:
					prglines.append(["mud", l4[1], l4[2], l4[3]])
				#6 nas: Increment value in a register by 1. (reg)
				case 6:
					prglines.append(["inc1", l4[1]])
				#7 nas: Decrement value in a register by 1. (reg)
				case 7:
					prglines.append(["dec1", l4[1]])
				#8 nas: Jump to label. (label)
				case 8:
					prglines.append(["jump", "label" + str(l4[1])])
				#9 nas: Jump to label if value in register is zero. (reg, label)
				case 9:
					prglines.append(["jump0", l4[1], "label" + str(l4[2])])
				#10 nas: Jump to label if value in register is not zero. (reg, label)
				case 10:
					prglines.append(["jump0not", l4[1], "label" + str(l4[2])])
		else:
			l2 = l.split("be")
			name = "label" + str(len(re.findall("na", l2[1])))
			labels[name] = len(prglines)		# line to jump to
			prglines.append([name])
	return [prglines, labels]

def run_program(prglines, labels, r0):
	reg = [0 for column in range(16)]
	reg[0] = r0
	steps = 0
	
	pc = 0			# program counter
	while pc < len(prglines):
		l = prglines[pc]
		match l[0]:
			#0 nas: Load immediate value into register. (val, dest_reg)
			case "load":
				reg[l[2]] = l[1]
			#1 na: Copy value from one register to another. (src_reg, dest_reg)
			case "copy":
				reg[l[2]] = reg[l[1]]
			#2 nas: Add values from two registers and store result in a third register. (src_reg1, src_reg2, dest_reg)
			case "add":
				reg[l[3]] = (reg[l[1]] + reg[l[2]]) % max_val
			#3 nas: Subtract values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
			case "sub":
				reg[l[3]] = (reg[l[1]] - reg[l[2]]) % max_val
			#4 nas: Multiply values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
			case "mult":
				reg[l[3]] = (reg[l[1]] * reg[l[2]]) % max_val
			#5 nas: Modulo values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
			case "mud":
				if reg[l[2]] == 0:
					reg[l[3]] = 0
				else:
					reg[l[3]] = reg[l[1]] % reg[l[2]]
			#6 nas: Increment value in a register by 1. (reg)
			case "inc1":
				reg[l[1]] = (reg[l[1]] + 1) % max_val
			#7 nas: Decrement value in a register by 1. (reg)
			case "dec1":
				reg[l[1]] = (reg[l[1]] - 1) % max_val
			#8 nas: Jump to label. (label)
			case "jump":
				pc = labels[l[1]]
			#9 nas: Jump to label if value in register is zero. (reg, label)
			case "jump0":
				if reg[l[1]] == 0:
					pc = labels[l[2]]
			#10 nas: Jump to label if value in register is not zero. (reg, label)
			case "jump0not":
				if reg[l[1]] != 0:
					pc = labels[l[2]]
		pc += 1
		steps += 1
		if steps == max_steps:
			break
				
	print("steps:", steps, "\t\treg..:", reg)
	return steps

###########################################################################
# prep

file = input2
lines = get_input()

# convert program
[prglines, labels] = convert_lines_to_program(lines)

###########################################################################
# part 1

print("Part 1:")
start_r0 = 0
run_program(prglines, labels, start_r0)

###########################################################################
# part 2

print("Part 2:")
infinite = 0
max_r0 = 100
for start_r0 in range(max_r0):
	steps = run_program(prglines, labels, start_r0)
	if steps == max_steps:
		infinite += 1

print("Infinite programs:", infinite)

###########################################################################
# part 3

print("Part 3:")
