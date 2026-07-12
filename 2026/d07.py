###########################################################################
# import

import re

###########################################################################
# constants

input1 = "input_d07_tst.txt"
input2 = "input_d07.txt"

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

file = input2
lines = get_input()

moves = lines.pop(0)
lines.pop(0)
sushi = lines

###########################################################################
# part 1

r = 0
c = 0
sushi_no = 0
next_sushi = re.findall('[0-9]+', sushi[sushi_no])
[nsc, nsr] = next_sushi
for i in range(int(len(moves)/2)):
	match moves[i]:
		case ">":
			c += 1
		case "<":
			c -= 1
		case "^":
			r += 1
		case "v":
			r -= 1
	if int(nsr) == r and int(nsc) == c:
		sushi_no += 1
		next_sushi = re.findall('[0-9]+', sushi[sushi_no])
		[nsc, nsr] = next_sushi

print("Part 1:", sushi_no)

###########################################################################
# part 2

print("Part 2:")

###########################################################################
# part 3

print("Part 3:")
