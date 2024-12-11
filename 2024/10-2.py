with open("10-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read().strip()


rows: list[str] = text.splitlines()


def get_adjacent_tiles(tile: tuple[int, int]) -> list[tuple[int, int]]:
    tiles: list[tuple[int, int]] = []
    if tile[0] > 0:
        tiles.append((tile[0] - 1, tile[1]))
    if tile[0] < len(rows[0]) - 1:
        tiles.append((tile[0] + 1, tile[1]))
    if tile[1] > 0:
        tiles.append((tile[0], tile[1] - 1))
    if tile[1] < len(rows) - 1:
        tiles.append((tile[0], tile[1] + 1))
    return tiles


def get_value(tile: tuple[int, int]) -> int:
    return int(rows[tile[1]][tile[0]])


def valid_paths_from(
    tile: tuple[int, int],
    value: int,
) -> int:
    if value == 9:
        return 1
    amount = 0
    for adjacent_tile in get_adjacent_tiles(tile):
        adjacent_value = get_value(adjacent_tile)
        if adjacent_value == value + 1:
            amount += valid_paths_from(
                adjacent_tile,
                adjacent_value,
            )
    return amount


zeroes: list[tuple[int, int]] = []
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char == "0":
            zeroes.append((x, y))

count = 0
for zero in zeroes:
    count += valid_paths_from(zero, 0)

print(count)
