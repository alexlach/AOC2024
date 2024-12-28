# parse input
lines = open("10/input.txt").read().split("\n")
grid = [list(line) for line in lines if line]
grid_height = len(grid)
grid_width = len(grid[0])

zero_locs = [
    (i, j) for i in range(grid_height) for j in range(grid_width) if grid[i][j] == "0"
]


def bfs(grid, start, visit_once=False):
    queue = [start]
    visited = set() if visit_once else []

    while queue:
        i, j = queue.pop(0)
        if visit_once:
            visited.add((i, j))
        else:
            visited.append((i, j))

        current_num = int(grid[i][j])
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < len(grid)
                and 0 <= nj < len(grid[0])
                and int(grid[ni][nj]) == current_num + 1
                and (not visit_once or (ni, nj) not in visited)
            ):
                queue.append((ni, nj))
    return visited


# part 1
visited_locs = [
    loc for zero_loc in zero_locs for loc in bfs(grid, zero_loc, visit_once=True)
]
visited_9s = [loc for loc in visited_locs if grid[loc[0]][loc[1]] == "9"]
print(len(visited_9s))

# part 2
visited_locs = [
    loc for zero_loc in zero_locs for loc in bfs(grid, zero_loc, visit_once=False)
]
visited_9s = [loc for loc in visited_locs if grid[loc[0]][loc[1]] == "9"]
print(len(visited_9s))
