###########################################################################
# import

import copy 

###########################################################################
# constants

input1 = "input_d05.txt"

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def count_distinct(lines):
	x = 0
	y = 0
	distinct = 0
	while(lines[y][x] != "*"):
		newx = x
		newy = y
		match lines[y][x]:
			case ">":
				newx += 1
			case "<":
				newx -= 1
			case "v":
				newy += 1
			case "^":
				newy -= 1
		lines[y][x] = "*"
		x = newx
		y = newy
		distinct += 1
	return distinct

###########################################################################
# prep

file = input1

###########################################################################
# part 1

lines = get_input()
lines2 = []
for l in lines:
	lines2.append(list(l))
lines = lines2

distinct = count_distinct(lines)

print("Part 1:", distinct)

###########################################################################
# part 2

lines = get_input()
lines2 = []
for l in lines:
	lines2.append(list(l))
lines = lines2

xmax = len(lines[0]) - 1
ymax = len(lines) - 1
distinct_max = 0

for i in range(1, xmax):
	for j in range(1, ymax):
		for k in "<>v^":
			newlines = copy.deepcopy(lines)
			newlines[j][i] = k
			distinct = count_distinct(newlines)
			if distinct_max < distinct:
				distinct_max = distinct

print("Part 2:", distinct_max)

###########################################################################
# part 3

print("Part 3:")
