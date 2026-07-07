###########################################################################
# import

###########################################################################
# constants

drinkable = 60
heat_up_time = 1
cool_down_time = 5
input1 = "input_d01.txt"

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
lines = list(map(int, lines))

###########################################################################
# part 1

sum_of_heatings = 0
for temp in lines:
	if temp < drinkable:
		sum_of_heatings += drinkable - temp

print("Part 1:", sum_of_heatings)

###########################################################################
# part 2

sum_of_changes = 0
for temp in lines:
	if temp < drinkable:
		sum_of_changes += (drinkable - temp) * heat_up_time
	if drinkable < temp:
		sum_of_changes += (temp - drinkable) * cool_down_time

print("Part 2:", sum_of_changes)

###########################################################################
# part 3

no_of_lines = int(len(lines)/2)
lines1 = lines[:no_of_lines]
lines2 = lines[no_of_lines:]

sum_of_changes = 0
for i in range(no_of_lines):
	temp = lines1[i]
	drinkable_local = lines2[i]
	if temp < drinkable_local:
		sum_of_changes += (drinkable_local - temp) * heat_up_time
	if drinkable_local < temp:
		sum_of_changes += (temp - drinkable_local) * cool_down_time

print("Part 3:", sum_of_changes)

