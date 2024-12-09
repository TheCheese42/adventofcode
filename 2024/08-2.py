with open("08-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()


frequencies: dict[str, list[tuple[int, int]]] = {}
rows = text.splitlines()
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char != ".":
            if char not in frequencies:
                frequencies[char] = []
            frequencies[char].append((x, y))

map_width = len(rows[0])
map_height = len(rows)

antinodes: set[tuple[int, int]] = set()
for freq in frequencies.copy():
    coords = frequencies.pop(freq)
    for coord in coords.copy():
        coords.pop(0)
        for other_coord in coords:
            lowest_x = min(other_coord[0], coord[0])
            highest_x = max(other_coord[0], coord[0])
            lowest_y = min(other_coord[1], coord[1])
            highest_y = max(other_coord[1], coord[1])
            diff = (highest_x - lowest_x, highest_y - lowest_y)
            while True:
                new_diff = (diff[0] / 2, diff[1] / 2)
                if new_diff[0].is_integer() and new_diff[1].is_integer():
                    diff = (int(new_diff[0]), int(new_diff[1]))
                else:
                    break
            prev_an = coord
            while True:
                if coord[0] < other_coord[0]:
                    antinode = [prev_an[0] - diff[0], prev_an[1] - diff[1]]
                else:
                    antinode = [prev_an[0] + diff[0], prev_an[1] - diff[1]]
                an_tuple = (antinode[0], antinode[1])
                if not (
                    0 <= an_tuple[0] < map_width
                    and 0 <= an_tuple[1] < map_height
                ):
                    break
                if an_tuple != other_coord:
                    antinodes.add(an_tuple)
                prev_an = an_tuple
            prev_an = coord
            while True:
                if coord[0] < other_coord[0]:
                    antinode = [prev_an[0] + diff[0], prev_an[1] + diff[1]]
                else:
                    antinode = [prev_an[0] - diff[0], prev_an[1] + diff[1]]
                an_tuple = (antinode[0], antinode[1])
                if not (
                    0 <= an_tuple[0] < map_width
                    and 0 <= an_tuple[1] < map_height
                ):
                    break
                if an_tuple != other_coord:
                    antinodes.add(an_tuple)
                prev_an = an_tuple
            antinodes.add(coord)
            antinodes.add(other_coord)

print(len(antinodes))

# Uncomment for a visualization of the map

# for y, row in enumerate(rows):
#     print()
#     for x, char in enumerate(row):
#         for an in antinodes:
#             if (x, y) == an:
#                 print("#", end="")
#                 break
#         else:
#             print(char, end="")
# print()
