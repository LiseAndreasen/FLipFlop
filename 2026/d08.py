###########################################################################
# import

import functools

###########################################################################
# constants

input1 = "input_d08_tst.txt"
input2 = "input_d08.txt"

first_stoats = ["A", "B"]

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expand_stoats(s0, s1, gen):
	#print("gen", gen, "begin", s0, s1)
	new_stoats = []
	for r in rules:
		r0 = r[0]
		r1 = r[1]
		if (s0 == r0 and s1 == r1) or (s0 == r1 and s1 == r0):
			new_stoats.append(s0)
			for i in range(2,len(r)):
				new_stoats.append(r[i])
			break
	new_stoats.append(s1)
	
	# the caller will count s0 and s1
	if gen == 0:
		#print("gen", gen, "end", s0, new_stoats, s1)
		return len(new_stoats) - 2
	else:
		no_of_stoats = 1
		for s_no in range(len(new_stoats)-1):
			s0a = new_stoats[s_no]
			s1a = new_stoats[s_no+1]
			no = expand_stoats(s0a, s1a, gen - 1)
			#print("gen", gen - 1, s0a, no, s1a)
			no_of_stoats += no + 1
		#print("gen", gen, "end", s0, no_of_stoats, s1)
		return no_of_stoats - 2


###########################################################################
# prep

file = input2
lines = get_input()
rules = []
for l in lines:
	rules.append(l.split())

###########################################################################
# part 1

stoats = first_stoats
no_of_generations = 7
for j in range(no_of_generations):
	new_stoats = []
	for s in stoats:
		for r in rules:
			r0 = r[0]
			if s == r0:
				for i in range(1,len(r)):
					new_stoats.append(r[i])
				break
	stoats = new_stoats

print("Part 1:", len(new_stoats))

###########################################################################
# part 2

stoats = first_stoats
no_of_generations = 7
for j in range(no_of_generations):
	new_stoats = []
	for s_no in range(len(stoats)-1):
		s0 = stoats[s_no]
		s1 = stoats[s_no+1]
		for r in rules:
			r0 = r[0]
			r1 = r[1]
			if (s0 == r0 and s1 == r1) or (s0 == r1 and s1 == r0):
				new_stoats.append(s0)
				for i in range(2,len(r)):
					new_stoats.append(r[i])
				break
	new_stoats.append(stoats[len(stoats)-1])
	stoats = new_stoats

print("Part 2:", len(stoats))

###########################################################################
# part 3

stoats = first_stoats
no_of_generations = 21
no_of_stoats = 1
s0 = stoats[0]
s1 = stoats[1]
no_of_stoats = expand_stoats(s0, s1, no_of_generations - 1) + 2

print("Part 3:", no_of_stoats)
