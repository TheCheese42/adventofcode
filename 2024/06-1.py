with open("06-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

rows = text.splitlines()
guard_pos: list[int] = [0, 0]
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char == "^":
            guard_pos = [x, y]
            rows[y] = row.replace("^", ".")

coords: set[tuple[int, ...]] = set()
guard_facing = "top"
while True:
    coords.add(tuple(guard_pos))
    x, y = guard_pos
    if x == 0 and guard_facing == "left":
        break
    elif x == len(rows[0]) - 1 and guard_facing == "right":
        break
    elif y == 0 and guard_facing == "top":
        break
    elif y == len(rows) - 1 and guard_facing == "bottom":
        break
    elif guard_facing == "top" and rows[y - 1][x] == ".":
        guard_pos[1] -= 1
    elif guard_facing == "bottom" and rows[y + 1][x] == ".":
        guard_pos[1] += 1
    elif guard_facing == "left" and rows[y][x - 1] == ".":
        guard_pos[0] -= 1
    elif guard_facing == "right" and rows[y][x + 1] == ".":
        guard_pos[0] += 1
    elif guard_facing == "top" and rows[y - 1][x] == "#":
        guard_facing = "right"
    elif guard_facing == "bottom" and rows[y + 1][x] == "#":
        guard_facing = "left"
    elif guard_facing == "left" and rows[y][x - 1] == "#":
        guard_facing = "top"
    elif guard_facing == "right" and rows[y][x + 1] == "#":
        guard_facing = "bottom"

print(len(coords))
