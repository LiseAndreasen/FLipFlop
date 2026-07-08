###########################################################################
# import

###########################################################################
# constants

input1 = "input_d03_tst.txt"

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

###########################################################################
# part 3

