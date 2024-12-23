# parse input
lines = open("08/input.txt").read().split("\n")
grid = [list(line) for line in lines if line]
grid_height = len(grid)
grid_width = len(grid[0])

# map antenna positions
antenna_positions = {}
for i in range(grid_height):
    for j in range(grid_width):
        if grid[i][j] != ".":
            if grid[i][j] in antenna_positions:
                antenna_positions[grid[i][j]].append((i, j))
            else:
                antenna_positions[grid[i][j]] = [(i, j)]

print(antenna_positions)

# find antinodes for antenna pairs
antinodes = []
for frequency in antenna_positions:
    antenna_list = antenna_positions[frequency]
    for i in range(len(antenna_list)):
        for j in range(i):
            x1, y1 = antenna_list[i]
            x2, y2 = antenna_list[j]
            antinode_x = x2 + (x2 - x1)
            antinode_y = y2 + (y2 - y1)
            antinodes.append((antinode_x, antinode_y))
            x1, y1 = antenna_list[j]
            x2, y2 = antenna_list[i]
            antinode_x = x2 + (x2 - x1)
            antinode_y = y2 + (y2 - y1)
            antinodes.append((antinode_x, antinode_y))

# filter out of bounds antinodes
antinodes = [
    antinode
    for antinode in antinodes
    if antinode[0] >= 0
    and antinode[0] < grid_height
    and antinode[1] >= 0
    and antinode[1] < grid_width
]

print(len(set(antinodes)))  # remove duplicates

antinodes = []


def get_antinodes_p2(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)

    # Include the current antenna position
    antinodes.append((x2, y2))

    # Loop to calculate successive antinodes
    while 0 <= newx < grid_height and 0 <= newy < grid_width:
        antinodes.append((newx, newy))
        newx += x2 - x1
        newy += y2 - y1


for antenna_pair in antenna_positions.values():
    for i in range(len(antenna_pair)):
        for j in range(i):
            get_antinodes_p2(antenna_pair[i], antenna_pair[j])
            get_antinodes_p2(antenna_pair[j], antenna_pair[i])

print(len(set(antinodes)))
