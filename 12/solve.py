from collections import deque


def find_regions_and_perimeters(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    results = []

    for i in range(height):
        for j in range(width):
            if (i, j) not in seen:
                # process each region exactly once
                letter = grid[i][j]
                area = 0
                perimeter = 0
                queue = deque([(i, j)])
                seen.add((i, j))

                while queue:
                    ci, cj = queue.popleft()
                    area += 1

                    # count perimeter by checking neighbors
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = ci + di, cj + dj
                        if not (0 <= ni < height and 0 <= nj < width):
                            perimeter += 1
                        elif grid[ni][nj] != letter:
                            perimeter += 1
                        elif (ni, nj) not in seen:
                            seen.add((ni, nj))
                            queue.append((ni, nj))

                results.append((area, perimeter))

    return sum(area * perimeter for area, perimeter in results)


def find_regions_and_edges(grid):
    """
    For each contiguous region of identical letters, count how many sides
    it has. A side is a connected boundary in a single direction.
    Then return the sum of (area_of_region * sides_of_region) across all regions.
    """
    height, width = len(grid), len(grid[0])
    visited_global = set()
    total = 0

    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for r in range(height):
        for c in range(width):
            if (r, c) not in visited_global:
                # identify all cells in this region using BFS
                region_letter = grid[r][c]
                region_cells = set()
                queue = deque([(r, c)])
                area = 0

                # maps direction -> set of boundary cells exposed in that direction
                boundary_dict = {}

                while queue:
                    cr, cc = queue.popleft()
                    if (cr, cc) in region_cells:
                        continue
                    region_cells.add((cr, cc))
                    area += 1

                    for dr, dc in DIRS:
                        nr, nc = cr + dr, cc + dc
                        # if out-of-bounds or different letter -> boundary
                        if (
                            not (0 <= nr < height and 0 <= nc < width)
                            or grid[nr][nc] != region_letter
                        ):
                            # record boundary cell in the direction (dr,dc)
                            if (dr, dc) not in boundary_dict:
                                boundary_dict[(dr, dc)] = set()
                            boundary_dict[(dr, dc)].add((cr, cc))
                        else:
                            # same letter -> part of region
                            if (nr, nc) not in region_cells:
                                queue.append((nr, nc))

                sides = 0
                for direction, boundary_cells in boundary_dict.items():
                    visited_boundary = set()
                    for cell in boundary_cells:
                        if cell not in visited_boundary:
                            sides += 1  # found a new connected boundary side
                            queue_bdry = deque([cell])
                            while queue_bdry:
                                br, bc = queue_bdry.popleft()
                                if (br, bc) in visited_boundary:
                                    continue
                                visited_boundary.add((br, bc))

                                for ddr, ddc in DIRS:
                                    nbr, nbc = br + ddr, bc + ddc
                                    if (nbr, nbc) in boundary_cells and (
                                        nbr,
                                        nbc,
                                    ) not in visited_boundary:
                                        queue_bdry.append((nbr, nbc))

                total += area * sides

                visited_global |= region_cells

    return total


lines = open("12/input.txt").read().split("\n")
grid = [list(line) for line in lines if line]

# part 1
print(find_regions_and_perimeters(grid))

# part 2
print(find_regions_and_edges(grid))
