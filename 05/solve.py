rules, updates = open("05/input.txt").read().split("\n\n")
rules = [rule.split("|") for rule in rules.split("\n")]
updates = [update.split(",") for update in updates.split("\n")]


def validate_update(update, rules):
    for rule in rules:
        for i, page in enumerate(update):
            pages_before = update[:i]
            pages_after = update[i + 1 :]
            if (page in rule[0] and rule[1] in pages_before) or (
                page in rule[1] and rule[0] in pages_after
            ):
                return rule
    return None


valid_updates = [update for update in updates if validate_update(update, rules) is None]
middle_items = [update[len(update) // 2] for update in valid_updates]
print(sum([int(item) for item in middle_items]))

# Part 2
invalid_updates = [
    update for update in updates if validate_update(update, rules) is not None
]
fixed_updates = []
for update in invalid_updates:
    while True:
        status = validate_update(update, rules)
        if status is None:
            fixed_updates.append(update)
            break
        update[update.index(status[0])] = status[1]
        update[update.index(status[1])] = status[0]

middle_items = [update[len(update) // 2] for update in fixed_updates]
print(sum([int(item) for item in middle_items]))
