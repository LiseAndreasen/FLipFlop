###########################################################################
# import

from string import ascii_lowercase, ascii_uppercase 

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

def score_pwd(pwd, part):
	score = 0
	if any(c.islower() for c in pwd):
		score += 1
	if any(c.isupper() for c in pwd):
		score += 1
	if any(c.isdigit() for c in pwd):
		score += 1

	if 2 <= part:
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
	
	return score

def score_all(lines, part, c):
	max_score = 0
	max_pwd = ""
	score_sum = 0
	
	for pwd in lines:
		pwd_extra = pwd + extra
		score = score_pwd(pwd_extra, part)
		score_sum += score
		if max_score < score:
			max_score = score
			max_pwd = pwd
	return [max_pwd, score_sum]
	

###########################################################################
# prep

file = input1
lines = get_input()

###########################################################################
# part 1

part = 1
extra = ""
[max_pwd, score_sum] = score_all(lines, part, extra)
print("Part 1:", max_pwd)

###########################################################################
# part 2

part = 2
extra = ""
[max_pwd, score_sum] = score_all(lines, part, extra)
print("Part 2:", max_pwd)

###########################################################################
# part 3

part = 3
max_sum = 0
for extra in ascii_lowercase:
	[max_pwd, score_sum] = score_all(lines, part, extra)
	if max_sum < score_sum:
		max_sum = score_sum
for extra in ascii_uppercase:
	[max_pwd, score_sum] = score_all(lines, part, extra)
	if max_sum < score_sum:
		max_sum = score_sum
for e in range(10):
	extra = str(e)
	[max_pwd, score_sum] = score_all(lines, part, extra)
	if max_sum < score_sum:
		max_sum = score_sum
print("Part 3:", max_sum)
