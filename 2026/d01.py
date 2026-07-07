###########################################################################
# import

###########################################################################
# constants

drinkable = 60
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
# 

file = input1
lines = get_input()
lines = list(map(int, lines))
#print(lines)

sum_of_heatings = 0
for temp in lines:
	if temp < drinkable:
		sum_of_heatings += drinkable - temp

print(sum_of_heatings)

