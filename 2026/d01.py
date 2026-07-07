###########################################################################
# import

###########################################################################
# constants

drinkable = 60
heat_up_time = 1
cool_down_time = 5
input1 = "input_1_1.txt"

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

###########################################################################
# part 1

file = input1
lines = get_input()
lines = list(map(int, lines))

sum_of_heatings = 0
for temp in lines:
	if temp < drinkable:
		sum_of_heatings += drinkable - temp

print(sum_of_heatings)

###########################################################################
# part 2

sum_of_changes = 0
for temp in lines:
	if temp < drinkable:
		sum_of_changes += (drinkable - temp) * heat_up_time
	if drinkable < temp:
		sum_of_changes += (temp - drinkable) * cool_down_time

print(sum_of_changes)


