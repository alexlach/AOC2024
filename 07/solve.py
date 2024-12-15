lines = open("07/input.txt").read().split("\n")

targets = [int(line.split(": ")[0]) for line in lines]
params = [line.split(": ")[1].split(" ") for line in lines]


def try_operation(current_value, index, target, params, concat=False):
    if index == len(params):
        return current_value == target

    # multiplication
    if try_operation(current_value * params[index], index + 1, target, params, concat):
        return True

    # addition
    if try_operation(current_value + params[index], index + 1, target, params, concat):
        return True

    # concatenation
    if concat:
        concat_value = int(str(current_value) + str(params[index]))
        if try_operation(concat_value, index + 1, target, params, concat):
            return True

    return False


def is_possible(target, params, concat=False):
    params = [int(x) for x in params]
    return try_operation(params[0], 1, target, params, concat)


# part 1
print(
    sum(
        target for target, params in zip(targets, params) if is_possible(target, params)
    )
)

# part 2
print(
    sum(
        target
        for target, params in zip(targets, params)
        if is_possible(target, params, concat=True)
    )
)
