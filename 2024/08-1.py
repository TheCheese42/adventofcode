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
            an1 = [0, 0]
            if coord[0] < other_coord[0]:
                an1[0] = coord[0] - diff[0]
            else:
                an1[0] = coord[0] + diff[0]
            an1[1] = coord[1] - diff[1]
            an2 = [0, 0]
            if coord[0] < other_coord[0]:
                an2[0] = other_coord[0] + diff[0]
            else:
                an2[0] = other_coord[0] - diff[0]
            an2[1] = other_coord[1] + diff[1]

            if 0 <= an1[0] < map_width and 0 <= an1[1] < map_height:
                antinodes.add((an1[0], an1[1]))
            if 0 <= an2[0] < map_width and 0 <= an2[1] < map_height:
                antinodes.add((an2[0], an2[1]))

print(len(antinodes))
