lines = open("02/input.txt").read().split("\n")
lines = [[int(x) for x in line.split()] for line in lines]


def determine_if_safe(line):
    numbers = line
    if len(set(numbers)) != len(numbers):
        return False  # any repeating number means it's unsafe
    if numbers != sorted(numbers) and numbers != sorted(numbers, reverse=True):
        return False  # not increasing or decreasing means unsafe
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) > 3:
            return False  # difference greater than 3 means unsafe
    return True


print(sum(determine_if_safe(line) for line in lines))


def determine_if_safe_with_removal(line):
    if determine_if_safe(line):
        return True
    for i in range(len(line)):
        if determine_if_safe(line[:i] + line[i + 1 :]):
            return True
    return False


print(sum(determine_if_safe_with_removal(line) for line in lines))
