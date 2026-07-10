###########################################################################
# import

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

###########################################################################
# prep

file = input1
lines = get_input()
lines2 = []
for l in lines:
	lines2.append(list(l))
lines = lines2

###########################################################################
# part 1

x = 0
y = 0
distinct = 0
#print(lines[y][x])
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

print("Part 1:", distinct)

###########################################################################
# part 2

print("Part 2:")

###########################################################################
# part 3

print("Part 3:")
