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

def count_distinct(lines, illegal):
	orglines = copy.deepcopy(lines)
	
	x = 0
	y = 0
	if illegal:
		illegal_moves = 3
	else:
		illegal_moves = 0
	distinct = 0
	
	while(lines[y][x] != "*" or 0 < illegal_moves):
		newx = x
		newy = y
		if lines[y][x] == "*":
			if 0 < x < xmax and 0 < y < ymax:
				match orglines[y][x]:
					case ">":
						newy += 1
					case "<":
						newy -= 1
					case "v":
						newx -= 1
					case "^":
						newx += 1
				illegal_moves -= 1
				d = 0
			else:
				illegal_moves = 0		# stop moving
				d = 0
		else:			
			match lines[y][x]:
				case ">":
					newx += 1
				case "<":
					newx -= 1
				case "v":
					newy += 1
				case "^":
					newy -= 1
			d = 1
		lines[y][x] = "*"
		x = newx
		y = newy
		distinct += d
	return distinct

###########################################################################
# prep

file = input1
lines = get_input()
lines2 = []
for l in lines:
	lines2.append(list(l))

###########################################################################
# part 1

lines = copy.deepcopy(lines2)
illegal = False

distinct = count_distinct(lines, illegal)

print("Part 1:", distinct)

###########################################################################
# part 2

illegal = False

xmax = len(lines[0]) - 1
ymax = len(lines) - 1
distinct_max = 0

for i in range(1, xmax):
	for j in range(1, ymax):
		for k in "<>v^":
			newlines = copy.deepcopy(lines2)
			newlines[j][i] = k
			distinct = count_distinct(newlines, illegal)
			if distinct_max < distinct:
				distinct_max = distinct

print("Part 2:", distinct_max)

###########################################################################
# part 3

illegal = True

xmax = len(lines[0]) - 1
ymax = len(lines) - 1
distinct_max = 0

for i in range(1, xmax):
	for j in range(1, ymax):
		for k in "<>v^":
			newlines = copy.deepcopy(lines2)
			newlines[j][i] = k
			distinct = count_distinct(newlines, illegal)
			if distinct_max < distinct:
				distinct_max = distinct

print("Part 3:", distinct_max)
