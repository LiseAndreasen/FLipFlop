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
	for r in range(h):
		for c in range(w):
			no = no_stack.pop(0)
			card[r][c] = no
	return card

def print_card(card, w, h):
	for r in range(h):
		for c in range(w):
			print("%3s " % card[r][c], end="")
		print("")
	print("===========")

# register where the numbers occur on the cards
def register_numbers(cards, w, h, max):
	number_pos = [[] for _ in range(max+1)]
	for card in range(len(cards)):
		for r in range(h):
			for c in range(w):
				no = int(cards[card][r][c])
				number_pos[no] += [card, r, c]
	return number_pos

def count_bingos(card, w, h):
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
number_pos = register_numbers(cards, cw, ch, max_number)

# a choice: running through the numbers will change the cards

# run through the numbers, until enough bingos have occurred
no_of_bingos = [0 for _ in range(len(cards))]

for i in range(len(numbers)):
	no = int(numbers[i])
	pos = number_pos[no]
	[card, r, c] = pos
	cards[card][r][c] = bingo_mark
	no_of_bingos[card] = count_bingos(cards[card], cw, ch)
	if min_bingo_stop <= sum(no_of_bingos):
		break

print("Part 1:", no)

###########################################################################
# part 2

print("Part 2:")

###########################################################################
# part 3

print("Part 3:")
