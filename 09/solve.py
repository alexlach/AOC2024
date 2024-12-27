def parse_input(filename):
    line = open(filename).read()
    file_blocks = [int(x) for x in line[::2]]  # numbers
    empty_blocks = [int(x) for x in line[1::2]]  # dots

    return file_blocks, empty_blocks


def build_disk_map(file_blocks, empty_blocks):
    disk_map = []

    # Handle pairs of file and empty blocks
    for file_num, (file_size, empty_size) in enumerate(zip(file_blocks, empty_blocks)):
        disk_map.extend([str(file_num)] * file_size)
        disk_map.extend(["."] * empty_size)

    # handle last file block without empties after it
    disk_map.extend([str(len(file_blocks) - 1)] * file_blocks[-1])

    return disk_map


def consolidate_empty_blocks(disk_map):
    total_swaps = 0
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != ".":
            # find first empty block before this position
            for j in range(i):
                if disk_map[j] == ".":
                    disk_map[j], disk_map[i] = disk_map[i], disk_map[j]
                    total_swaps += 1
                    break
    return total_swaps


def consolidate_files(disk_map, file_blocks):
    # find all empty slots as ranges of start and end indices
    empty_ranges = []
    current_start = None

    for i, block in enumerate(disk_map):
        if block == ".":
            if current_start is None:
                current_start = i
        else:
            if current_start is not None:
                empty_ranges.append((current_start, i - 1))
                current_start = None

    if current_start is not None:
        empty_ranges.append((current_start, len(disk_map) - 1))

    # move files to earlier slots
    for file_id in range(len(file_blocks) - 1, 0, -1):
        file_size = file_blocks[file_id]

        # check if the file exists in the map
        if str(file_id) not in disk_map:
            continue

        current_start = min(
            i for i, block in enumerate(disk_map) if block == str(file_id)
        )

        for i, (start, end) in enumerate(empty_ranges):
            slot_size = end - start + 1
            # only move if:
            # 1. the file fits in the slot
            # 2. the slot is to the left of the current position
            if file_size <= slot_size and start < current_start:
                current_positions = [
                    j for j, block in enumerate(disk_map) if block == str(file_id)
                ]
                # move file into this slot
                for j in range(file_size):
                    disk_map[start + j] = str(file_id)
                    disk_map[current_positions[j]] = "."

                # remove the range we just filled
                empty_ranges.pop(i)

                # add the range we just emptied
                old_start = current_positions[0]
                old_end = current_positions[-1]
                empty_ranges.append((old_start, old_end))

                # the leftover part of the slot is anything we didn't occupy
                leftover_start = start + file_size
                if leftover_start <= end:
                    empty_ranges.append((leftover_start, end))

                empty_ranges.sort()
                break


file_blocks, empty_blocks = parse_input("09/input.txt")

# Part 1
disk_map = build_disk_map(file_blocks, empty_blocks)
consolidate_empty_blocks(disk_map)
checksum_a = sum(i * int(x) for i, x in enumerate(disk_map) if x != ".")
print(f"Part 1 answer: {checksum_a}")

# Part 2
disk_map = build_disk_map(file_blocks, empty_blocks)
consolidate_files(disk_map, file_blocks)
checksum_b = sum(i * int(x) for i, x in enumerate(disk_map) if x != ".")
print(f"Part 2 answer: {checksum_b}")
