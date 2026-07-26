###########################################################################
# import

import numpy as np

###########################################################################
# constants

input1 = "input_d11_tst.txt"
input2 = "input_d11.txt"
input3 = "input_d11_tst2.txt"
LEFT = 0
UP = 1
RIGHT = 2
no_growth = "XX"
empty = ".."
STEM = "##"
dirs = [[0, -1], [-1, 0], [0, 1]]

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def print_map(map):
	for m in map:
		print("".join(m))
	print("=====")

def is_stem(candidate, trees):
	if candidate in trees:
		return True
	else:
		return False

def grow_tree(tree, configurations, sprouts, stems):
	new_sprouts = []
	# grow new sprouts from old sprouts
	for sprout in sprouts:
		[r, c] = sprout
		id = int(tree[r][c])
		configuration = configurations[id]
		for i in range(len(dirs)):
			dir = dirs[i]
			[dr, dc] = dir
			r_new = r + dr
			c_new = c + dc
			# if there's growth in this direction
			if configuration[i] != no_growth:
				# if there's free space to grow
				if tree[r_new][c_new] == empty:
					tree[r_new][c_new] = configuration[i]
					new_sprouts.append([r_new, c_new])
					continue
				# if there isn't free space,
				# but the existing id is lower than this id
				if not is_stem(tree[r_new][c_new], trees) and tree[r_new][c_new] < configuration[i]:
					tree[r_new][c_new] = configuration[i]
		tree[r][c] = tree_id
		stems.append([r,c])
	return [tree, new_sprouts, stems]

def calculate_energy(tree, stems, sprouts):
	energy_out = 3 * (len(stems) + len(sprouts))
	energy_in = 0
	for c in range(max_age*2+1):
		column_shade = 0
		for r in range(max_age+1):
			if is_stem(tree[r][c], trees):
				# height above ground
				h = min(max_age - r + 1, max_height)
				e = stem_contribution - column_shade
				energy_in += e * h
				column_shade += 1
				if column_shade == column_shade_max:
					break
	return [energy_in, energy_out]

###########################################################################
# prep

file = input1
lines = get_input()

ascii_0 = 97
trees = {}
tree_no = 0
for i in range(len(lines)):
	tree_id = chr(tree_no + ascii_0) + chr(tree_no + ascii_0)
	configurations = {}
	if i % 3 == 0:
		# all the tops
		tops = lines[i].split()
	if i % 3 == 1:
		# all the bottoms
		bottoms = lines[i].split()
		for j in range(len(tops)):
			this_up = tops.pop(0)
			this_left = bottoms.pop(0)
			this_id = int(bottoms.pop(0))
			this_right = bottoms.pop(0)
			configurations[this_id] = [this_left, this_up, this_right]
		trees[tree_id] = configurations
		tree_no += 1

###########################################################################
# part 1

max_age = 100
energy_age = 5
first_tree = "00"
column_shade_max = 3
stem_contribution = 3
max_height = 10

bio_mass = 0

# grow each tree max_age years, according to the configurations
for tree_id in trees:
	configurations = trees[tree_id]
	# grid representing tree
	tree = [[empty for column in range(max_age*2+1)]
	                      for row in range(max_age+1)]
	tree[max_age][max_age] = first_tree
	# lists of sprouts and stems
	sprouts = [[max_age, max_age]]
	stems = []
	# keep track of age of tree and energies
	age = 0
	energy_in = 0
	energy_out = 0
	while energy_out <= energy_in and age < max_age:
		# grow the tree
		age += 1
		[tree, sprouts, stems] = grow_tree(tree, configurations, sprouts, stems)
		# calculate the new energy needs
		if energy_age <= age:
			[energy_in, energy_out] = calculate_energy(tree, stems, sprouts)
	print("tree dies at age", age)
	bio_mass += len(stems) + len(sprouts)
					
print("Part 1:", bio_mass)

###########################################################################
# part 2

print("Part 2:")

###########################################################################
# part 3

print("Part 3:")
