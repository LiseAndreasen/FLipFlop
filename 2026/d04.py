###########################################################################
# import

###########################################################################
# constants

input1 = "input_d04.txt"

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

###########################################################################
# prep

file = input1
lines = get_input()

###########################################################################
# part 1

h = len(lines)
cut = 400
ground = 1
above_cut = h - cut - ground
no_of_leaves = 0
for i in range(above_cut):
	if "|-o" in lines[i] or "o-|" in lines[i]:
		no_of_leaves += 1
print("Part 1:", no_of_leaves)

###########################################################################
# part 2

swaps = -1
side = ""
for i in lines:
	if "|-o" in i:
		if side != "right":
			swaps += 1
			side = "right"
	if "o-|" in i:
		if side != "left":
			swaps += 1
			side = "left"		

print("Part 2:", swaps)

###########################################################################
# part 3

print("Part 3:")
