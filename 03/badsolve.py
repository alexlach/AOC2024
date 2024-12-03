text = open("03/input.txt").read()

# print(text)

# match mul(x,y) where x and y are numbers
import re

# matches = re.findall(r"mul\((\d+),(\d+)\)", text)
# print(matches)

# print(sum(int(x) * int(y) for x, y in matches))


def find_all_occurrences(string, substring):
    """Finds all occurrences of a substring in a string."""
    indices = []
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index + 1
    return indices


# find indexes of don't() where it occurs in the text
dont_indexes = find_all_occurrences(text, "don't()")
print(dont_indexes)

do_indexes = find_all_occurrences(text, "do()")
print(do_indexes)

# mark any text between don't() and do() for deletion
delete_ranges = []
for i in range(len(dont_indexes)):
    current_dont_index = dont_indexes[i]
    greater_do_indexes = [
        do_index for do_index in do_indexes if do_index > current_dont_index
    ]
    min_greater_do_index = min(greater_do_indexes) if greater_do_indexes else None
    if min_greater_do_index:
        delete_ranges.append((current_dont_index, min_greater_do_index))
    else:
        delete_ranges.append((current_dont_index, None))


print(delete_ranges)

# delete the text in the ranges
for start, end in delete_ranges:
    if end:
        text = text[:start] + text[end:]

matches = re.findall(r"mul\((\d+),(\d+)\)", text)
# print(matches)

print(sum(int(x) * int(y) for x, y in matches))
