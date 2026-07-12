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
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
	61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
	139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
	223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

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

# count number of gears in group next to coordinates
# bluetooth output
def count_group(map, r, c):
	local_map = copy.deepcopy(map)
	cell1 = [r, c]
	cells = [cell1]
	no_of_gears = 0

	while 0 < len(cells):
		cell = cells.pop(0)
		[rl, cl] = cell
		gear = local_map[rl][cl]
		if gear == "3" or gear.isupper():
			if gear == "3":
				no_of_gears += 1
			for dir in dirs:
				[dr, dc] = dir
				char = get_value(local_map, rl + dr, cl + dc)
				if char == "3":
					cells.append([rl+dr, cl+dc])
			local_map[rl][cl] = "*"
	
	return no_of_gears

# returns _ when the coordinates are outside the map
def get_value(map, r, c):
	if r < 0 or c < 0:
		return "_"
	if len(map) <= r:
		return "_"
	if len(map[0]) <= c:
		return "_"
	return map[r][c]

def turn_gears(map, part):
	match part:
		case 1:
			all_gears = "#"
			all_lights = "*"
			all_bluetooth = ""
			prime_rule = False
		case 2:
			all_gears = "#3"
			all_lights = "*"
			all_bluetooth = "abcdefghijklmnopqrstuvwxyz"
			prime_rule = False
		case 3:
			all_gears = "#3"
			all_lights = "*"
			all_bluetooth = "abcdefghijklmnopqrstuvwxyz"
			prime_rule = True
	
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
			if char in all_gears:
				if turn == "R":
					turns[r+dr][c+dc] = "L"
				else:
					turns[r+dr][c+dc] = "R"
				cells.append([r+dr, c+dc])
			if char in all_lights:
				if turn == "R":
					turns[r+dr][c+dc] = "1"
				else:
					turns[r+dr][c+dc] = "0"
			if char in all_bluetooth:
				upper_char = char.upper()
				upper_cell = find_char(upper_char, map)
				[ru, cu] = upper_cell
				if prime_rule:
					gear_count = count_group(map, ru, cu)
					if gear_count in primes:
						continue
				if turn == "R":
					turns[r+dr][c+dc] = "L"
					turns[ru][cu] = "R"
				else:
					turns[r+dr][c+dc] = "R"
					turns[ru][cu] = "L"
				cells.append([ru, cu])
	
	# look for the lights, turn the sequence of lights into a binary number
	
	lights = "".join(list(itertools.chain.from_iterable(turns)))
	lights = re.sub('[^01]', '', lights)
	final_state = int(lights, 2)
	return final_state

###########################################################################
# prep

file = input2
lines = get_input()
map = []
for l in lines:
	map.append(list(l))

chars1 = "".join(list(itertools.chain.from_iterable(map)))
chars2 = ''.join(sorted(set(chars1)))
print("Unique characters in input:", chars2, "\n")

###########################################################################
# part 1

part = 1
final_state = turn_gears(map, part)
print("Part 1:", final_state)

###########################################################################
# part 2

part = 2
final_state = turn_gears(map, part)
print("Part 2:", final_state)

###########################################################################
# part 3

part = 3
final_state = turn_gears(map, part)
print("Part 3:", final_state)
