###########################################################################
# import

import copy
import itertools
import re

###########################################################################
# constants

input1 = "input_d06_tst.txt"
input2 = "input_d06.txt"
dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def find_char(char, map):
	for r in range(len(map)):
		for c in range(len(map[0])):
			if map[r][c] == char:
				return [r, c]

def print_map(map):
	for m in map:
		print("".join(m))

def get_value(map, r, c):
	if r < 0 or c < 0:
		return ""
	if len(map) <= r:
		return ""
	if len(map[0]) <= c:
		return ""
	return map[r][c]

###########################################################################
# prep

file = input2
lines = get_input()
map = []
for l in lines:
	map.append(list(l))

chars1 = "".join(list(itertools.chain.from_iterable(map)))
chars2 = ''.join(sorted(set(chars1)))
print("Unique characters in input:", chars2)

###########################################################################
# part 1

turns = copy.deepcopy(map)
cell1 = find_char("S", turns)
[r, c] = cell1
turns[r][c] = "L"
cells = [cell1]

# turn gears into directions, L or R
# turn lights into high or low, 1 or 0

while 0 < len(cells):
	cell = cells.pop(0)
	[r, c] = cell
	turn = turns[r][c]
	for dir in dirs:
		[dr, dc] = dir 
		char = get_value(turns, r + dr, c + dc)
		match char:
			case "#":
				if turn == "R":
					turns[r+dr][c+dc] = "L"
				else:
					turns[r+dr][c+dc] = "R"
				cells.append([r+dr, c+dc])
			case "*":
				if turn == "R":
					turns[r+dr][c+dc] = "1"
				else:
					turns[r+dr][c+dc] = "0"
			case "R":
				do = 0
			case "L":
				do = 0
			case "h":
				do = 0
			case "l":
				do = 0
			case _:
				turns[r+dr][c+dc] = " "

# look for the lights, turn the sequence of lights into a binary number

lights = "".join(list(itertools.chain.from_iterable(turns)))
lights = re.sub('[^01]', '', lights)
final_state = int(lights, 2)

print("Part 1:", final_state)

###########################################################################
# part 2

print("Part 2:")

###########################################################################
# part 3

print("Part 3:")
