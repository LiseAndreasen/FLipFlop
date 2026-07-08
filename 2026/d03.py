###########################################################################
# import

###########################################################################
# constants

input1 = "input_d03.txt"

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

###########################################################################
# part 1

max_score = 0
max_pwd = ""

for pwd in lines:
	score = 0
	if any(c.islower() for c in pwd):
		score += 1
	if any(c.isupper() for c in pwd):
		score += 1
	if any(c.isdigit() for c in pwd):
		score += 1
	score *= len(pwd)
	if max_score < score:
		max_score = score
		max_pwd = pwd

print("Part 1:", max_pwd)

###########################################################################
# part 2

max_score = 0
max_pwd = ""

for pwd in lines:
	score = 0
	if any(c.islower() for c in pwd):
		score += 1
	if any(c.isupper() for c in pwd):
		score += 1
	if any(c.isdigit() for c in pwd):
		score += 1
		
	digit_seen = []
	for c in pwd:
		if c.isdigit():
			if c not in digit_seen:
				digit_seen.append(c)
	if len(digit_seen) == 1 and digit_seen[0] == "7":
		score += 7
	
	prev = ""
	max_prev_no = 1
	for c in pwd:
		if c == prev:
			prev_no += 1
		else:
			prev_no = 1
		prev = c
		if max_prev_no < prev_no:
			max_prev_no = prev_no
	if 3 <= max_prev_no:
		score += max_prev_no * max_prev_no
	
	if "red" in pwd or "green" in pwd or "blue" in pwd:
		score *= 3
	
	score *= len(pwd)
	if max_score < score:
		max_score = score
		max_pwd = pwd

print("Part 2:", max_pwd)

###########################################################################
# part 3

