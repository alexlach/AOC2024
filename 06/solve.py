from collections import Counter

lines = open("06/input.txt").read().split("\n")
grid = [list(line) for line in lines if line]

original_guard_pos = [
    (i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "^"
][0]


def in_grid(pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


traversed = []
guard_dir = (-1, 0)
guard_pos = original_guard_pos
while in_grid(guard_pos):
    traversed.append(guard_pos)
    next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
    if not in_grid(next_pos):
        break  # guard is leaving the grid
    if grid[next_pos[0]][next_pos[1]] == "#":
        guard_dir = (guard_dir[1], -guard_dir[0])  # turn clockwise
    else:
        guard_pos = next_pos  # move

print(len(Counter(traversed).items()))


def infinite_loop(grid, guard_pos):
    def in_grid(pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

    obstacle_turn = []
    guard_dir = (-1, 0)
    while in_grid(guard_pos):
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        if not in_grid(next_pos):
            return False  # guard is leaving the grid
        elif grid[next_pos[0]][next_pos[1]] == "#":
            guard_dir = (guard_dir[1], -guard_dir[0])  # turn clockwise
            if [guard_pos[0], guard_pos[1], next_pos[0], next_pos[1]] in obstacle_turn:
                return True
            else:
                obstacle_turn.append(
                    [guard_pos[0], guard_pos[1], next_pos[0], next_pos[1]]
                )
        else:
            guard_pos = next_pos  # move
    return False


loop_solutions = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            modified_grid = [row.copy() for row in grid]
            modified_grid[i][j] = "#"
            guard_pos = original_guard_pos
            loop = infinite_loop(modified_grid, guard_pos)
            if loop:
                loop_solutions.append((i, j))

print(len(loop_solutions))
