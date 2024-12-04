from collections import Counter

lines = open("04/input.txt").read().split("\n")
grid = [list(line) for line in lines if line]


def check_direction(word, row, col, row_d, col_d, grid):
    if (
        row + (len(word) - 1) * row_d < 0
        or row + (len(word) - 1) * row_d >= len(grid)
        or col + (len(word) - 1) * col_d < 0
        or col + (len(word) - 1) * col_d >= len(grid[0])
    ):
        return None

    for i in range(len(word)):
        if grid[row + i * row_d][col + i * col_d] != word[i]:
            return None
    return (row + row_d, col + col_d)


def search_grid(grid, word, directions):
    indices = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for row_d, col_d in directions:
                loc = check_direction(word, row, col, row_d, col_d, grid)
                if loc:
                    indices.append(loc)

    return indices


# Search for "XMAS"
xmas_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
xmas_count = len(search_grid(grid, "XMAS", xmas_directions))
print(xmas_count)

# Search for "MAS"
mas_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
mas_indices = search_grid(grid, "MAS", mas_directions)
print(len(index for index, count in Counter(mas_indices).items() if count > 1))
