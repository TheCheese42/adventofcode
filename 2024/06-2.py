with open("06-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

rows = text.splitlines()
guard_pos: list[int] = [0, 0]
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char == "^":
            guard_pos = [x, y]
            rows[y] = row.replace("^", ".")


def makes_stuck(initial_pos: list[int], rows_: list[str]) -> bool:
    guard_status: list[tuple[tuple[int, ...], str]] = []
    guard_facing = "top"
    #print(rows_)
    while True:
        #print(initial_pos, guard_facing)
        guard_status.append((tuple(initial_pos), guard_facing))
        if guard_status.count(guard_status[-1]) > 1:
            return True
        x, y = initial_pos
        if x == 0 and guard_facing == "left":
            break
        elif x == len(rows_[0]) - 1 and guard_facing == "right":
            break
        elif y == 0 and guard_facing == "top":
            break
        elif y == len(rows_) - 1 and guard_facing == "bottom":
            break
        elif guard_facing == "top" and rows_[y - 1][x] == ".":
            initial_pos[1] -= 1
        elif guard_facing == "bottom" and rows_[y + 1][x] == ".":
            initial_pos[1] += 1
        elif guard_facing == "left" and rows_[y][x - 1] == ".":
            initial_pos[0] -= 1
        elif guard_facing == "right" and rows_[y][x + 1] == ".":
            initial_pos[0] += 1
        elif guard_facing == "top" and rows_[y - 1][x] == "#":
            guard_facing = "right"
        elif guard_facing == "bottom" and rows_[y + 1][x] == "#":
            guard_facing = "left"
        elif guard_facing == "left" and rows_[y][x - 1] == "#":
            guard_facing = "top"
        elif guard_facing == "right" and rows_[y][x + 1] == "#":
            guard_facing = "bottom"
    return False


count = 0
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if x % 10 == 0:
            print(x, y)
        if char == "#":
            continue
        if (x, y) == (guard_pos[0], guard_pos[1]):
            continue
        new_rows = rows.copy()
        new_row = list(row)
        new_row[x] = "#"
        new_rows[y] = "".join(new_row)
        if makes_stuck(guard_pos.copy(), new_rows):
            count += 1

# Won't take longer than 3 hours
print(count)
