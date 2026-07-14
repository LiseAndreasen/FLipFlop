###########################################################################
# import

from dijkstra import Graph

###########################################################################
# constants

input1 = "input_d09_tst.txt"
input2 = "input_d09.txt"
wall = "#"
empty = "."
start = "S"
end = "E"

dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]

###########################################################################
# functions

def get_input():
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

# convert row/column to a unique id
def map_id(r,c,h):
	return c * h + r

# returns _ when the coordinates are outside the map
def get_value(map, r, c):
	if r < 0 or c < 0:
		return "_"
	if len(map) <= r:
		return "_"
	if len(map[0]) <= c:
		return "_"
	return map[r][c]

def create_graph(map, part):
	global start_coord, end_coord
	gGraph = [[0 for column in range(all_cells)]
	                      for row in range(all_cells)]
	
	for r in range(len(map)):
		for c in range(len(map[0])):
			id = map_id(r,c,len(map))
			char = map[r][c]
			if char == wall:
				continue
			if char == start:
				start_coord = id
			if char == end:
				end_coord = id
			for dir in dirs:
				[dr, dc] = dir
				r_new = r + dr
				c_new = c + dc
				char_neigh = get_value(map, r_new, c_new)
				id_neigh = map_id(r_new,c_new,len(map))
				if char_neigh == "_":
					continue
				if char_neigh == wall:
					continue
				gGraph[id][id_neigh] = 1
				if part == 2:
					while char_neigh != "_" and char_neigh != wall:
						r_new += dr
						c_new += dc
						char_neigh = get_value(map, r_new, c_new)
						id_neigh = map_id(r_new,c_new,len(map))
					# 1 step too much
					r_new -= dr
					c_new -= dc 
					id_neigh = map_id(r_new,c_new,len(map))
					gGraph[id][id_neigh] = 1
		
	return gGraph

###########################################################################
# prep

file = input2
lines = get_input()
map = []
for l in lines:
	map.append(list(l))

###########################################################################
# part 1

part = 1

# convert map to graph

print("Part 1:")
print("Create graph for map")

all_cells = len(map) * len(map[0])
start_coord = -1
end_coord = -1
gGraph = create_graph(map, part)

g = Graph(all_cells)
g.graph = gGraph

# dijkstra!

print"Go Dijkstra"
g.dijkstra(start_coord, end_coord)

###########################################################################
# part 2

part = 2

# convert map to graph

print("Part 2:")
print("Create graph for map")

all_cells = len(map) * len(map[0])
start_coord = -1
end_coord = -1
gGraph = create_graph(map, part)

g = Graph(all_cells)
g.graph = gGraph

# dijkstra!

print"Go Dijkstra"
g.dijkstra(start_coord, end_coord)

###########################################################################
# part 3

print("Part 3:")
