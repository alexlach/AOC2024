stones = [int(stone) for stone in open("11/input.txt").read().split()]
stones_dict = {stone: stones.count(stone) for stone in set(stones)}


def evolve(stones_dict, blink_count):
    for _ in range(blink_count):
        new_dict = {}
        for stone, count in stones_dict.items():
            stone_str = str(stone)
            digit_count = len(stone_str)

            if stone == 0:
                new_stones = [1]
            elif digit_count % 2 == 0:
                mid = digit_count // 2
                new_stones = [int(stone_str[:mid]), int(stone_str[mid:])]
            else:
                new_stones = [stone * 2024]

            # update counts
            for new_stone in new_stones:
                new_dict[new_stone] = new_dict.get(new_stone, 0) + count

        stones_dict = new_dict
    return stones_dict


# part 1
print(sum(evolve(stones_dict, 25).values()))

# part 2
print(sum(evolve(stones_dict, 75).values()))
