###########################################################################
# import

###########################################################################
# constants

input1 = "input_d12_tst.txt"
input2 = "input_d12.txt"
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

# create bingo card, size w x h
def create_card(numbers, w, h):
	card = [[0 for column in range(w)] for row in range(h)]
	no_stack = numbers.split(" ")
	# row, column
	for r in range(h):
		for c in range(w):
			no = no_stack.pop(0)
			card[r][c] = no
	return card

def create_cube(numbers, d, w, h):
	cube = [[[0 for plane in range(d)] for column in range(w)] for row in range(h)]
	# plane, row, column
	for p in range(d):
		for r in range(h):
			for c in range(w):
				no = c + r * w + p * w * h
				cube[p][r][c] = numbers[no]
	return cube

def print_card(card, w, h):
	for r in range(h):
		for c in range(w):
			if card[r][c] == bingo_mark:
				print("\033[31m%3s\033[0m " % "XXX", end="")
			else:
				print("%3s " % card[r][c], end="")
		print("")
	print("===========")

# register where the numbers occur on the cards
def register_numbers_card(cards, w, h, max):
	number_pos = [[] for _ in range(max+1)]
	for card in range(len(cards)):
		for r in range(h):
			for c in range(w):
				no = int(cards[card][r][c])
				number_pos[no] += [card, r, c]
	return number_pos

def register_numbers_cube(cubes, d, w, h, max):
	number_pos = [[] for _ in range(max+1)]
	for cube in range(len(cubes)):
		for p in range(d):
			for r in range(h):
				for c in range(w):
					no = int(cubes[cube][p][r][c])
					number_pos[no] += [cube, p, r, c]
	return number_pos

def count_bingos_card(card, w, h):
	bingos = 0
	
	# rows
	for r in range(h):
		bingo = True
		for c in range(w):
			if card[r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	
	# columns
	for c in range(w):
		bingo = True
		for r in range(h):
			if card[r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			bingos += 1
	
	# diagonals
	bingo = True
	for c in range(w):
		r = c
		if card[r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1

	bingo = True
	for c in range(w):
		r = w - c - 1
		if card[r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		bingos += 1
	
	return bingos

def count_bingos_cube(cube, d, w, h):
	bingos = 0
	
	# straight
	# cp-r
	for c in range(w):
		for p in range(d):
			bingo = True
			for r in range(h):
				if cube[p][r][c] != bingo_mark:
					bingo = False
					break
			if bingo:
				#print("bingo! straight cp-r", c, p)
				bingos += 1
	
	# cr-p
	for c in range(w):
		for r in range(h):
			bingo = True
			for p in range(d):
				if cube[p][r][c] != bingo_mark:
					bingo = False
					break
			if bingo:
				#print("bingo! straight cr-p", c, r)
				bingos += 1
	
	# pr-c
	for p in range(d):
		for r in range(h):
			bingo = True
			for c in range(w):
				if cube[p][r][c] != bingo_mark:
					bingo = False
					break
			if bingo:
				#print("bingo! straight pr-c", p, r)
				bingos += 1

	# diagonal in plane, ascending
	# c-pr
	for c in range(w):
		bingo = True
		for p in range(d):
			r = p
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			#print("bingo! diagonal ascending c-pr", c)
			bingos += 1

	# p-cr
	for p in range(d):
		bingo = True
		for c in range(w):
			r = c
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			#print("bingo! ascending p-cr", p)
			bingos += 1

	# r-cp
	for r in range(h):
		bingo = True
		for c in range(w):
			p = c
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			#print("bingo! ascending r-cp", r)
			bingos += 1
	
	# diagonal in plane, descending
	# c-pr
	for c in range(w):
		bingo = True
		for p in range(d):
			r = d - p - 1
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			#print("bingo! descending c-pr", c)
			bingos += 1

	# p-cr
	for p in range(d):
		bingo = True
		for c in range(w):
			r = w - c - 1
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			#print("bingo! descending p-cr", p)
			bingos += 1

	# r-cp
	for r in range(h):
		bingo = True
		for c in range(w):
			p = w - c - 1
			if cube[p][r][c] != bingo_mark:
				bingo = False
				break
		if bingo:
			#print("bingo! descending r-cp", r)
			bingos += 1
	
	# diagonal from corner to opposite corner
	bingo = True
	for c in range(w):
		p = c
		r = c
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		#print("bingo! corner2corner c+p+r+")
		bingos += 1

	bingo = True
	for c in range(w):
		p = w - c - 1
		r = c
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		#print("bingo! corner2corner c+p-r+")
		bingos += 1
	
	bingo = True
	for c in range(w):
		p = c
		r = h - c - 1
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		#print("bingo! corner2corner c+p+r-")
		bingos += 1

	bingo = True
	for c in range(w):
		p = w - c - 1
		r = h - c - 1
		if cube[p][r][c] != bingo_mark:
			bingo = False
			break
	if bingo:
		#print("bingo! corner2corner c+p-r-")
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

cw = 5					# card width
ch = 5					# card height
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
	cards.append(create_card(l, cw, ch))

# register where the numbers occur on the cards
number_pos = register_numbers_card(cards, cw, ch, max_number)

# a choice: running through the numbers will change the cards

# run through the numbers, until enough bingos have occurred
no_of_bingos = [0 for _ in range(len(cards))]

for i in range(len(numbers)):
	no = int(numbers[i])
	pos = number_pos[no]
	[card, r, c] = pos
	cards[card][r][c] = bingo_mark
	no_of_bingos[card] = count_bingos_card(cards[card], cw, ch)
	if min_bingo_stop <= sum(no_of_bingos):
		break

print("Part 1:", no)
# test: 49

###########################################################################
# part 2

cd = 5					# cube depth

# create bingo cubes
cubes = []
for i in range(0, len(lines), cd):
	cube_flat = []
	for j in range(i, i + cd):
		cube_flat += lines[j].split(" ")
	cubes.append(create_cube(cube_flat, cd, cw, cw))

# register where the numbers occur on the cubes
number_pos = register_numbers_cube(cubes, cd, cw, ch, max_number)

# a choice: running through the numbers will change the cubes

# run through the numbers, until enough bingos have occurred
no_of_bingos = [0 for _ in range(len(cubes))]

for i in range(len(numbers)):
	no = int(numbers[i])
	pos = number_pos[no]
	[cube, p, r, c] = pos
	cubes[cube][p][r][c] = bingo_mark
	old_bingo_no = no_of_bingos[cube]
	no_of_bingos[cube] = count_bingos_cube(cubes[cube], cd, cw, ch)
	#if old_bingo_no < no_of_bingos[cube]:
	#	print(old_bingo_no, no_of_bingos[cube])
	#	for p in range(cd):
	#		print_card(cubes[cube][p], cw, ch)
	if min_bingo_stop <= sum(no_of_bingos):
		break

print("Part 2:", no)
# test: 63

###########################################################################
# part 3

print("Part 3:")
