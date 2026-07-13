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

file = input1
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

print("Part 2:")

###########################################################################
# part 3

print("Part 3:")
