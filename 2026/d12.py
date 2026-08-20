###########################################################################
# import

###########################################################################
# constants

input1 = "input_d12_tst.txt"
input2 = "input_d12.txt"
input3 = "input_d12_tst2.txt"
test = False
bingo_mark = "X"

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

# create bingo card, size sz x sz
def create_card(numbers, sz):
	card = [[0 for column in range(sz)] for row in range(sz)]
	no_stack = numbers.split(" ")
	# row, column
	for r in range(sz):
		for c in range(sz):
			no = no_stack.pop(0)
			card[r][c] = no
	return card

def create_cube(numbers, sz):
	cube = [[[0 for plane in range(sz)] for column in range(sz)] for row in range(sz)]
	# plane, row, column
	for p in range(sz):
		for r in range(sz):
			for c in range(sz):
				no = c + r * sz + p * sz * sz
				cube[p][r][c] = numbers[no]
	return cube

def print_card(card, sz):
	for r in range(sz):
		for c in range(sz):
			if card[r][c] == bingo_mark:
				print("\033[31m%3s\033[0m " % "XXX", end="")
			else:
				print("%3s " % card[r][c], end="")
		print("")
	print("===========")

# register where the numbers occur on the cards
def register_numbers_card(cards, sz, max):
	number_pos = [[] for _ in range(max+1)]
	for card in range(len(cards)):
		for r in range(sz):
			for c in range(sz):
				no = int(cards[card][r][c])
				number_pos[no] += [card, r, c]
	return number_pos

def register_numbers_cube(cubes, sz, max):
	number_pos = [[] for _ in range(max+1)]
	for cube in range(len(cubes)):
		for p in range(sz):
			for r in range(sz):
				for c in range(sz):
					no = int(cubes[cube][p][r][c])
					number_pos[no] += [cube, p, r, c]
	return number_pos

def register_numbers_hypercube(hypercube, sz, max):
	number_pos = [[] for _ in range(max+1)]
	for y in range(sz):
		for p in range(sz):
			for r in range(sz):
				for c in range(sz):
					no = int(hypercube[y][p][r][c])
					number_pos[no] += [y, p, r, c]
	return number_pos

###########################################################################
def count_bingos_card(card, sz):
	bingos = 0
	
	# rows
	for r in range(sz):
		bingo = True
		for c in range(sz):
			if card[r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	
	# columns
	for c in range(sz):
		bingo = True
		for r in range(sz):
			if card[r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	
	# diagonals
	bingo = True
	for c in range(sz):
		r = c
		if card[r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1

	bingo = True
	for c in range(sz):
		r = sz - c - 1
		if card[r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	
	return bingos

###########################################################################
def count_bingos_cube(cube, sz):
	bingos = 0
	
	# straight
	# cp-r
	for c in range(sz):
		for p in range(sz):
			bingo = True
			for r in range(sz):
				if cube[p][r][c] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	
	# cr-p
	for c in range(sz):
		for r in range(sz):
			bingo = True
			for p in range(sz):
				if cube[p][r][c] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	
	# pr-c
	for p in range(sz):
		for r in range(sz):
			bingo = True
			for c in range(sz):
				if cube[p][r][c] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1

	# diagonal in plane, ascending
	# c-pr
	for c in range(sz):
		bingo = True
		for p in range(sz):
			r = p
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	# p-cr
	for p in range(sz):
		bingo = True
		for c in range(sz):
			r = c
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	# r-cp
	for r in range(sz):
		bingo = True
		for c in range(sz):
			p = c
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	
	# diagonal in plane, descending
	# c-pr
	for c in range(sz):
		bingo = True
		for p in range(sz):
			r = sz - p - 1
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	# p-cr
	for p in range(sz):
		bingo = True
		for c in range(sz):
			r = sz - c - 1
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	# r-cp
	for r in range(sz):
		bingo = True
		for c in range(sz):
			p = sz - c - 1
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	
	# diagonal from corner to opposite corner
	bingo = True
	for c in range(sz):
		p = c
		r = c
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1

	bingo = True
	for c in range(sz):
		p = sz - c - 1
		r = c
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	
	bingo = True
	for c in range(sz):
		p = c
		r = sz - c - 1
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1

	bingo = True
	for c in range(sz):
		p = sz - c - 1
		r = sz - c - 1
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1

	return bingos

###########################################################################
def count_bingos_hypercube(hypercube, sz):
	bingos = 0
	
	#######################################################################
	# 3 constant variables, 1 varies
	# r varies
	for y in range(sz):
		for p in range(sz):
			for c in range(sz):
				bingo = True
				for r in range(sz):
					if hypercube[y][p][c][r] != bingo_mark:
						bingo = False
						break
				if bingo:
					bingos += 1
	# c varies
	for y in range(sz):
		for p in range(sz):
			for r in range(sz):
				bingo = True
				for c in range(sz):
					if hypercube[y][p][c][r] != bingo_mark:
						bingo = False
						break
				if bingo:
					bingos += 1
	# p varies
	for y in range(sz):
		for c in range(sz):
			for r in range(sz):
				bingo = True
				for p in range(sz):
					if hypercube[y][p][c][r] != bingo_mark:
						bingo = False
						break
				if bingo:
					bingos += 1
	# y varies
	for p in range(sz):
		for c in range(sz):
			for r in range(sz):
				bingo = True
				for y in range(sz):
					if hypercube[y][p][c][r] != bingo_mark:
						bingo = False
						break
				if bingo:
					bingos += 1

	#######################################################################
	# 2 constant variables, the other 2 equal or opposed
	# y and p constant, r and c equal
	for y in range(sz):
		for p in range(sz):
			bingo = True
			for r in range(sz):
				c = r
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# r and c opposed
	for y in range(sz):
		for p in range(sz):
			bingo = True
			for r in range(sz):
				c = sz - r - 1
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# y and r constant, p and c equal
	for y in range(sz):
		for r in range(sz):
			bingo = True
			for p in range(sz):
				c = p
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# p and c opposed
	for y in range(sz):
		for r in range(sz):
			bingo = True
			for p in range(sz):
				c = sz - p - 1
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# y and c constant, p and r equal
	for y in range(sz):
		for c in range(sz):
			bingo = True
			for p in range(sz):
				r = p
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# p and r opposed
	for y in range(sz):
		for c in range(sz):
			bingo = True
			for p in range(sz):
				r = sz - p - 1
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# p and r constant, y and c equal
	for p in range(sz):
		for r in range(sz):
			bingo = True
			for y in range(sz):
				c = y
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# y and c opposed
	for p in range(sz):
		for r in range(sz):
			bingo = True
			for y in range(sz):
				c = sz - y - 1
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# p and c constant, y and r equal
	for p in range(sz):
		for c in range(sz):
			bingo = True
			for y in range(sz):
				r = y 
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# y and r opposed
	for p in range(sz):
		for c in range(sz):
			bingo = True
			for y in range(sz):
				r = sz - y - 1
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# r and c constant, y and p equal
	for r in range(sz):
		for c in range(sz):
			bingo = True
			for y in range(sz):
				p = y	
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1
	# y and p opposed
	for r in range(sz):
		for c in range(sz):
			bingo = True
			for y in range(sz):
				p = sz - y - 1
				if hypercube[y][p][c][r] != bingo_mark:
					bingo = False
					break
			if bingo:
				bingos += 1

	#######################################################################
	# 1 constant variables, the other 3 equal or opposed
	# y constant, p = r = c
	for y in range(sz):
		bingo = True
		for p in range(sz):
			r = p
			c = p
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# p = r = - c
	for y in range(sz):
		bingo = True
		for p in range(sz):
			r = p
			c = sz - p - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# p = - r = c
	for y in range(sz):
		bingo = True
		for p in range(sz):
			r = sz - p - 1
			c = p
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# -p = r = c
	for y in range(sz):
		bingo = True
		for p in range(sz):
			r = sz - p - 1
			c = sz - p - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	#######################################################################
	# p constant, y = r = c
	for p in range(sz):
		bingo = True
		for y in range(sz):
			r = y
			c = y
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# y = r = - c
	for p in range(sz):
		bingo = True
		for y in range(sz):
			r = y
			c = sz - y - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# y = - r = c
	for p in range(sz):
		bingo = True
		for y in range(sz):
			r = sz - y - 1
			c = y
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# - y = r = c
	for p in range(sz):
		bingo = True
		for y in range(sz):
			r = sz - y - 1
			c = sz - y - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	#######################################################################
	# r constant, y = p = c
	for r in range(sz):
		bingo = True
		for y in range(sz):
			p = y
			c = y
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# y = p = - c
	for r in range(sz):
		bingo = True
		for y in range(sz):
			p = y
			c = sz - y - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# y = - p = c
	for r in range(sz):
		bingo = True
		for y in range(sz):
			p = sz - y - 1
			c = y
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# - y = p = c
	for r in range(sz):
		bingo = True
		for y in range(sz):
			p = sz - y - 1
			c = sz - y - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	#######################################################################
	# c constant, y = p = r
	for c in range(sz):
		bingo = True
		for y in range(sz):
			p = y
			r = y
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# y = p = - r
	for c in range(sz):
		bingo = True
		for y in range(sz):
			p = y
			r = sz - y - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# y = - p = r
	for c in range(sz):
		bingo = True
		for y in range(sz):
			p = sz - y - 1
			r = y
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	# - y = p = r
	for c in range(sz):
		bingo = True
		for y in range(sz):
			p = sz - y - 1
			r = sz - y - 1
			if hypercube[y][p][c][r] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1

	#######################################################################
	# 0 constant variables, all 4 equal or opposed
	# y = p = r = c
	for y in range(sz):
		bingo = True
		p = y
		r = y
		c = y
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# y = p = r = - c
	for y in range(sz):
		bingo = True
		p = y
		r = y
		c = sz - y - 1
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# y = p = - r = c
	for y in range(sz):
		bingo = True
		p = y
		r = sz - y - 1
		c = y
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# y = - p = r = c
	for y in range(sz):
		bingo = True
		p = sz - y - 1
		r = y
		c = y
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# - y = p = r = c
	for y in range(sz):
		bingo = True
		p = sz - y - 1
		r = sz - y - 1
		c = sz - y - 1
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# y = p = - r = - c
	for y in range(sz):
		bingo = True
		p = y
		r = sz - y - 1
		c = sz - y - 1
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# y = - p = r = - c
	for y in range(sz):
		bingo = True
		p = sz - y - 1
		r = y
		c = sz - y - 1
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	# - y = p = r = - c
	for y in range(sz):
		bingo = True
		p = sz - y - 1
		r = sz - y - 1
		c = y
		if hypercube[y][p][c][r] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1

	return bingos

###########################################################################
# prep

if test:
	file = input1
else:
	file = input2
lines = get_input()

###########################################################################
# part 1

sz = 5					# card width/heigh

min_bingo_stop = 5		# stop after this number of bingos

# what is the highest number occurring
if test:
	max_number = 125
else:
	max_number = 625

# which numbers will be run
numbers = []
while 0 < len(lines):
	tmp = lines.pop(0)
	if 0 < len(tmp):
		numbers += tmp.split(" ")
	else:
		break

# create bingo cards
cards = []
for l in lines:
	cards.append(create_card(l, sz))

# register where the numbers occur on the cards
number_pos = register_numbers_card(cards, sz, max_number)

# a choice: running through the numbers will change the cards

# run through the numbers, until enough bingos have occurred
no_of_bingos = [0 for _ in range(len(cards))]

for i in range(len(numbers)):
	no = int(numbers[i])
	pos = number_pos[no]
	[card, r, c] = pos
	cards[card][r][c] = bingo_mark
	no_of_bingos[card] = count_bingos_card(cards[card], sz)
	if min_bingo_stop <= sum(no_of_bingos):
		break

print("Part 1:", no)
# test: 49

###########################################################################
# part 2

# create bingo cubes
cubes = []
for i in range(0, len(lines), sz):
	cube_flat = []
	for j in range(i, i + sz):
		cube_flat += lines[j].split(" ")
	cubes.append(create_cube(cube_flat, sz))

# register where the numbers occur on the cubes
number_pos = register_numbers_cube(cubes, sz, max_number)

# a choice: running through the numbers will change the cubes

# run through the numbers, until enough bingos have occurred
no_of_bingos = [0 for _ in range(len(cubes))]

for i in range(len(numbers)):
	no = int(numbers[i])
	pos = number_pos[no]
	[cube, p, r, c] = pos
	cubes[cube][p][r][c] = bingo_mark
	no_of_bingos[cube] = count_bingos_cube(cubes[cube], sz)
	if min_bingo_stop <= sum(no_of_bingos):
		break

print("Part 2:", no)
# test: 63

###########################################################################
# part 3

if test:
	file = input3
	lines = get_input()
	min_bingo_stop = 1
	max_number = 625
	numbers = []
	while 0 < len(lines):
		tmp = lines.pop(0)
		if 0 < len(tmp):
			numbers += tmp.split(" ")
		else:
			break

# create bingo hypercube
hypercube = [[[[]]]]
hypercube = [[[[0 for ydim in range(sz)] for plane in range(sz)] for column in range(sz)] for row in range(sz)]

cube_numbers = []
for l in lines:
	cube_numbers += l.split(" ")

for y in range(sz):
	for p in range(sz):
		for r in range(sz):
			for c in range(sz):
				no = c + r * sz + p * sz * sz + y * sz * sz * sz
				hypercube[y][p][r][c] = cube_numbers[no]

# register where the numbers occur on the cubes
number_pos = register_numbers_hypercube(hypercube, sz, max_number)

# a choice: running through the numbers will change the hypercube

# run through the numbers, until enough bingos have occurred
for i in range(len(numbers)):
	no = int(numbers[i])
	pos = number_pos[no]
	[y, p, r, c] = pos
	hypercube[y][p][r][c] = bingo_mark
	no_of_bingos = count_bingos_hypercube(hypercube, sz)
	if min_bingo_stop <= no_of_bingos:
		break

print("Part 3:", no)
