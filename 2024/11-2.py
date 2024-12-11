from collections import Counter
from functools import cache

with open("11-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read().strip()


@cache
def process_stone(stone: int) -> tuple[int, ...]:
    new_stones: list[int] = []
    if stone == 0:
        new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
        digits = str(stone)
        num_per_half = len(digits) // 2
        new_stones.append(int(digits[num_per_half:]))
        new_stones.append(int(digits[:num_per_half]))
    else:
        new_stones.append(stone * 2024)
    return tuple(new_stones)


@cache
def process_stone_list(stones: tuple[int], countdown: int) -> int:
    if countdown < 1:
        return len(stones)
    count = 0
    for stone in stones:
        processed = process_stone(stone)
        count += process_stone_list(processed, countdown - 1)

    return count


stones = [int(i) for i in text.split()]

print(process_stone_list(tuple(stones), 75))
