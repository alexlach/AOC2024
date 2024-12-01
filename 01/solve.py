lines = open("01/input.txt").read().split("\n")
list1, list2 = zip(*[line.split("  ") for line in lines])

# part 1
list1 = sorted([int(x) for x in list1])
list2 = sorted([int(x) for x in list2])
diffs = [abs(a - b) for a, b in zip(list1, list2)]
print(sum(diffs))

# part 2
freq = {}
for item in list2:
    freq[item] = freq.get(item, 0) + 1

print(sum(item * freq.get(item, 0) for item in list1))
