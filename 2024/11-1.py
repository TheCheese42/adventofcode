from functools import cache

with open("11-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read().strip()


@cache
def process_stone(stone: int) -> list[int]:
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
    return new_stones


@cache
def process_stone_list(stones: tuple[int]) -> list[int]:
    new_stones: list[int] = []
    for stone in stones:
        new_stones.extend(process_stone(stone))
    return new_stones


stones: list[int] = [int(i) for i in text.split()]

for _ in range(75):
    print(_)
    stones = process_stone_list(tuple(stones))

print(len(stones))
