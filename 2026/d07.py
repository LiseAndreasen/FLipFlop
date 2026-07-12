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

def snake_walk(moves, sushi, part):
	r = 0
	c = 0
	sushi_no = 0
	next_sushi = re.findall('[0-9]+', sushi[sushi_no])
	[nsc, nsr] = next_sushi
	snake = [[r,c]]
	eaten = 0
	if part == 3:
		moves_no = len(moves)
	else:
		moves_no = int(len(moves)/2)
	
	for i in range(moves_no):
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
			if sushi_no < len(sushi):
				next_sushi = re.findall('[0-9]+', sushi[sushi_no])
				[nsc, nsr] = next_sushi
			else:
				[nsc, nsr] = [-1,-1]
		else:
			# snake won't grow
			snake.pop(0)
		if part == 2:
			if [r,c] in snake:
				# snake dies
				return [sushi_no, len(snake), eaten * len(snake)]
		if part == 3:
			if [r,c] in snake:
				# snake eats segment, rest falls off
				while [r,c] in snake:
					snake.pop(0)
				# then remove 1 more segment
				snake.pop(0)
				eaten += 1
		snake.append([r,c])
	
	return [sushi_no, len(snake), eaten * len(snake)]

###########################################################################
# prep

file = input2
lines = get_input()

moves = lines.pop(0)
lines.pop(0)
sushi = lines

###########################################################################
# part 1

part = 1
[sushi_no, length, eaten] = snake_walk(moves, sushi, part)
print("Part 1:", sushi_no)

###########################################################################
# part 2

part = 2
[sushi_no, length, eaten] = snake_walk(moves, sushi, part)
print("Part 2:", length)

###########################################################################
# part 3

part = 3
[sushi_no, length, eaten] = snake_walk(moves, sushi, part)
print("Part 3:", eaten)
