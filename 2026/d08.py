###########################################################################
# import

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

print("Part 3:")
