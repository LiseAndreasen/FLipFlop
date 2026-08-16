###########################################################################
# import

import numpy as np
import re
from time import sleep

###########################################################################
# constants

input1 = "input_d11_tst.txt"
input2 = "input_d11b.txt"
input3 = "input_d11_tst2.txt"
LEFT = 0
UP = 1
RIGHT = 2
no_growth = "XX"
empty = "...."
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
		for c in m:
			if is_stem(c, initial_trees):
				print("#", end="")
				continue
			if c == empty:
				print(".", end="")
				continue
			print("@", end="")
		print("")
	print("=====")
	sleep(3)

def is_stem(candidate, initial_trees):
	c1 = candidate[:2]
	c2 = candidate[2:3]
	if c1 == STEM and c2 in initial_trees:
		return True
	else:
		return False

def is_no_growth(candidate, initial_trees):
	c = candidate[:2]
	if c == no_growth:
		return True
	else:
		return False

def is_foreign(candidate, tree_id):
	# look from 3rd character in string
	c = candidate[2:]
	if c == tree_id:
		return False
	else:
		return True

def grow_tree(tree, configurations, sprouts, stems):
	if len(sprouts) == 0:
		return [tree, sprouts, stems]
		
	root = sprouts[0]
	[r_root, c_root] = root
	tree_id = tree[r_root][c_root][2:]
	
	new_sprouts = []
	# grow new sprouts from old sprouts
	for sprout in sprouts:
		[r, c] = sprout
		id1 = tree[r][c][:3]
		id2 = tree[r][c][3:]
		configuration = configurations[id1]
		for i in range(len(dirs)):
			dir = dirs[i]
			[dr, dc] = dir
			r_new = r + dr
			c_new = c + dc
			# if there's growth in this direction
			if not is_no_growth(configuration[i], initial_trees):
				# if there's free space to grow
				if tree[r_new][c_new] == empty:
					tree[r_new][c_new] = configuration[i] + id2
					new_sprouts.append([r_new, c_new])
					continue
				# if there isn't free space,
				# because of another tree, stop
				if is_foreign(tree[r_new][c_new], tree_id):
					continue
				# if there isn't free space,
				# but the existing id is lower than this id
				if not is_stem(tree[r_new][c_new], initial_trees) and tree[r_new][c_new][:3] < configuration[i]:
					tree[r_new][c_new] = configuration[i] + id2
		tree[r][c] = STEM + tree_id
		stems.append([r,c])
	return [tree, new_sprouts, stems]

def calculate_energy(tree, stems, sprouts):
	root = stems[0]
	[r_root, c_root] = root
	tree_id = tree[r_root][c_root][2:]
	
	energy_out = 3 * (len(stems) + len(sprouts))
	energy_in = 0
	for c in range(c_root - max_age, c_root + max_age + 1):
		column_shade = 0
		for r in range(max_age+1):
			if is_stem(tree[r][c], initial_trees):
				# if my stem
				if tree[r][c][2:] == tree_id:
					# height above ground
					h = min(max_age - r + 1, max_height)
					e = stem_contribution - column_shade
					energy_in += e * h
				column_shade += 1
				if column_shade == column_shade_max:
					break
	return [energy_in, energy_out]

def drop_sprouts(tree_field, alive):
	field_height = len(tree_field)
	field_width = len(tree_field[0])
	dropped_sprouts = [empty for column in range(field_width)]
	tree_types = {}
	for t in alive:
		t0 = t[0]
		tree_types[t0] = 0
	for c in range(field_width):
		for r in range(field_height):
			cell = tree_field[r][c]
			if not is_stem(cell, initial_trees) and cell != empty:
				tree_type = cell[2:3]
				tree_id = tree_type + str(tree_types[tree_type])
				sprout = first_tree + tree_id
				dropped_sprouts[c] = sprout
				tree_types[tree_type] += 1
				continue
	return dropped_sprouts

def grow_forest_small():
	bio_mass = 0
	singleton = "0"
	
	# grow each tree max_age years, according to the configurations
	for tree_id in initial_trees:
		configurations = initial_trees[tree_id]
		# grid representing tree
		tree = [[empty for column in range(max_age*2+1)]
		                      for row in range(max_age+1)]
		tree[max_age][max_age] = first_tree + tree_id + singleton
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
		#print(tree)
	
	return bio_mass
	
def grow_forest(generations):
	no_of_trees = len(initial_trees)
	
	width = max_age*2*generations+tree_distance*(no_of_trees-1)+1
	height = max_age+1
	tree_field = [[empty for column in range(width)]
	                      for row in range(height)]
	singleton = "0"
	
	# plant trees, 1st generation
	tree_no = 0
	sprouts = {}
	stems = {}
	alive = {}
	for tree_id in initial_trees:
		new_tree_id = tree_id + singleton
		tree_field[max_age][max_age*generations+tree_distance*tree_no] = first_tree + new_tree_id
		sprouts[new_tree_id] = [[max_age, max_age*generations+tree_distance*tree_no]]
		stems[new_tree_id] = []
		alive[new_tree_id] = True
		tree_no += 1
		
	while 0 < generations:
		age = 0
		trees_alive = len(alive)
		while age < max_age and 0 < trees_alive:
			age += 1
			for tree_id in alive:
				if alive[tree_id]:
					configurations = initial_trees[tree_id[:1]]
					[tree_field, new_sprouts, new_stems] = grow_tree(tree_field, configurations, sprouts[tree_id], stems[tree_id])
					sprouts[tree_id] = new_sprouts
					stems[tree_id] = new_stems
					if len(new_sprouts) == 0:
						alive[tree_id] = False
						trees_alive -= 1
						print("tree", tree_id, "dies at age", age, "size", len(stems[tree_id]) + len(sprouts[tree_id]), "-", trees_alive, "trees still alive")
			# calculate energy for each tree
			if energy_age <= age:
				for tree_id in alive:
					if alive[tree_id]:
						[energy_in, energy_out] = calculate_energy(tree_field, stems[tree_id], sprouts[tree_id])
						if energy_in < energy_out:
							alive[tree_id] = False
							trees_alive -= 1
							print("tree", tree_id, "dies at age", age, "size", len(stems[tree_id]) + len(sprouts[tree_id]), "-", trees_alive, "trees still alive")
			# last line of while age
			
		generations -= 1
		if 0 < generations:
			print("\nStart new generation")
			new_trees = drop_sprouts(tree_field, alive)
			tree_field = [[empty for column in range(width)]
		                      for row in range(height)]
			sprouts = {}
			stems = {}
			alive = {}
			for s in range(len(new_trees)):
				cell = new_trees[s]
				if cell != empty:
					tree_id = cell[2:]
					tree_field[max_age][s] = cell
					sprouts[tree_id] = [[max_age, s]]
					stems[tree_id] = []
					alive[tree_id] = True
		# last line of while generations
	
	bio_mass = 0
	for tree_id in alive:
		bio_mass += len(stems[tree_id]) + len(sprouts[tree_id])
	return bio_mass

###########################################################################
# prep

file = input2
lines = get_input()

ascii_0 = 97
initial_trees = {}
tree_no = 0
for i in range(len(lines)):
	tree_id = chr(tree_no + ascii_0)
	configurations = {}
	if i % 3 == 0:
		# all the tops
		tops = lines[i].split()
	if i % 3 == 1:
		# all the bottoms
		bottoms = lines[i].split()
		for j in range(len(tops)):
			this_up = tops.pop(0) + tree_id
			this_left = bottoms.pop(0) + tree_id
			this_id = bottoms.pop(0) + tree_id
			this_right = bottoms.pop(0) + tree_id
			configurations[this_id] = [this_left, this_up, this_right]
		initial_trees[tree_id] = configurations
		tree_no += 1

###########################################################################
# part 1
print("Part 1 begin")
max_age = 100
energy_age = 5
first_tree = "00"
column_shade_max = 3
stem_contribution = 3
max_height = 10

bio_mass = grow_forest_small()
print("Part 1:", bio_mass)

# input1: tree dies at 67, bio mass 1224

###########################################################################
# part 2

print("\nPart 2 begin")
tree_distance = 10
generations = 1

bio_mass = grow_forest(generations)
print("Part 2:", bio_mass)

# input3: bio mass 1431

###########################################################################
# part 3

print("\nPart 3 begin")
generations = 3

bio_mass = grow_forest(generations)
print("\nPart 3:", bio_mass)

# input3: bio mass 4122
# input2: 10430 is incorrect
