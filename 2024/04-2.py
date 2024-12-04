# You gotta admit, this code is crazily efficient

with open("04-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

coords: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]] = []
rows = text.splitlines()
length = len(rows[0])
num_rows = len(rows)
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == "M":
            if (
                j < length - 2
                and row[j:j + 4] == "MAS"
            ):
                # Right
                coords.append(((j, i), (j+1, i), (j+2, i)))
            if (
                j > 1
                and row[j - 3:j + 1] == "SAM"
            ):
                # Left
                coords.append(((j, i), (j-1, i), (j-2, i)))
            if (
                i > 1
                and rows[i - 1][j] == "A"
                and rows[i - 2][j] == "S"
            ):
                # Up
                coords.append(((j, i), (j, i-1), (j, i-2)))
            if (
                i < num_rows - 2
                and rows[i + 1][j] == "A"
                and rows[i + 2][j] == "S"
            ):
                # Down
                coords.append(((j, i), (j, i+1), (j, i+2)))
            if (
                i > 1
                and j > 1
                and rows[i - 1][j - 1] == "A"
                and rows[i - 2][j - 2] == "S"
            ):
                # Upper left
                coords.append(((j, i), (j-1, i-1), (j-2, i-2)))
            if (
                i > 1
                and j < length - 2
                and rows[i - 1][j + 1] == "A"
                and rows[i - 2][j + 2] == "S"
            ):
                # Upper right
                coords.append(((j, i), (j+1, i-1), (j+2, i-2)))
            if (
                i < num_rows - 2
                and j > 1
                and rows[i + 1][j - 1] == "A"
                and rows[i + 2][j - 2] == "S"
            ):
                # Lower left
                coords.append(((j, i), (j-1, i+1), (j-2, i+2)))
            if (
                i < num_rows - 2
                and j < length - 2
                and rows[i + 1][j + 1] == "A"
                and rows[i + 2][j + 2] == "S"
            ):
                # Lower right
                coords.append(((j, i), (j+1, i+1), (j+2, i+2)))


def is_dia(x: tuple[int, int], y: tuple[int, int], z: tuple[int, int]) -> bool:
    hor = False
    ver = False
    if x[1] > y[1] or z[1] > y[1]:
        ver = True
    if x[0] > y[0] or z[0] > y[0]:
        hor = True
    return ver and hor


count = 0
already_matched: list[
    tuple[tuple[tuple[int, int], tuple[int, int],tuple[int, int]],
          tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]
    ] = []
for i, coord in enumerate(coords):
    print(f"Processing {i + 1}/{len(coords)} ({count} matched)")
    x, y, z = coord
    for other in coords:
        stop = False
        for matched in already_matched.copy():
            if coord in matched and other in matched:
                stop = True
                break
            if y[1] - 5 > matched[0][1][1]:
                already_matched.remove(matched)
        if stop:
            continue
        if other == coord:
            continue
        ox, oy, oz = other
        if y == oy:
            if is_dia(x, y, z) == is_dia(ox, oy, oz):
                count += 1
                already_matched.append((coord, other))

print(count - 1)  # Off by one
