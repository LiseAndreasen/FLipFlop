###########################################################################
# import

import numpy as np

###########################################################################
# constants

input1 = "input_d02.txt"

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
moves = lines[0]

###########################################################################
# part 1

# actual wall pos is 0-99
last_wall = 100
wall = np.zeros_like(range(last_wall))
robot_pos = 0

no_of_moves = len(moves)
for i in range(no_of_moves):
	if moves[i] == ">":
		robot_pos = (robot_pos + 1) % last_wall
	if moves[i] == "<":
		robot_pos = (robot_pos - 1) % last_wall
	wall[robot_pos] += 1

max_wall = np.max(wall)
max_pos = np.argmax(wall) + 1		# adjust wall pos, now 1-100
print("Part 1:", max_wall * max_pos)

###########################################################################
# part 2

wall = np.zeros_like(range(last_wall))
robot_pos = 0
wall_pos = 0
wall_hit = 0

for i in range(no_of_moves):
	j = no_of_moves - i - 1
	if moves[i] == ">":
		robot_pos = (robot_pos + 1) % last_wall
	if moves[i] == "<":
		robot_pos = (robot_pos - 1) % last_wall
	if moves[j] == ">":
		wall_pos = (wall_pos + 1) % last_wall
	if moves[j] == "<":
		wall_pos = (wall_pos - 1) % last_wall
	if robot_pos == wall_pos:
		wall_hit += 1

print("Part 2:", wall_hit)

###########################################################################
# part 3

# instead of moving the wall, move the robot more

wall = np.zeros_like(range(last_wall))
robot_pos = 0

for i in range(no_of_moves):
	j = no_of_moves - i - 1
	if moves[i] == ">":
		robot_pos = (robot_pos + 1) % last_wall
	if moves[i] == "<":
		robot_pos = (robot_pos - 1) % last_wall
	if moves[j] == ">":
		robot_pos = (robot_pos - 1) % last_wall
	if moves[j] == "<":
		robot_pos = (robot_pos + 1) % last_wall
	wall[robot_pos] += 1

max_wall = np.max(wall)
max_pos = np.argmax(wall) + 1		# adjust wall pos, now 1-100
print("Part 3:", max_wall * max_pos)
