# You gotta admit, this code is crazily efficient

with open("04-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

count = 0
rows = text.splitlines()
length = len(rows[0])
num_rows = len(rows)
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == "X":
            if (
                j < length - 3
                and row[j:j + 4] == "XMAS"
            ):
                # Right
                count += 1
            if (
                j > 2
                and row[j - 3:j + 1] == "SAMX"
            ):
                # Left
                count += 1
            if (
                i > 2
                and rows[i - 1][j] == "M"
                and rows[i - 2][j] == "A"
                and rows[i - 3][j] == "S"
            ):
                # Up
                count += 1
            if (
                i < num_rows - 3
                and rows[i + 1][j] == "M"
                and rows[i + 2][j] == "A"
                and rows[i + 3][j] == "S"
            ):
                # Down
                count += 1
            if (
                i > 2
                and j > 2
                and rows[i - 1][j - 1] == "M"
                and rows[i - 2][j - 2] == "A"
                and rows[i - 3][j - 3] == "S"
            ):
                # Upper left
                count += 1
            if (
                i > 2
                and j < length - 3
                and rows[i - 1][j + 1] == "M"
                and rows[i - 2][j + 2] == "A"
                and rows[i - 3][j + 3] == "S"
            ):
                # Upper right
                count += 1
            if (
                i < num_rows - 3
                and j > 2
                and rows[i + 1][j - 1] == "M"
                and rows[i + 2][j - 2] == "A"
                and rows[i + 3][j - 3] == "S"
            ):
                # Lower left
                count += 1
            if (
                i < num_rows - 3
                and j < length - 3
                and rows[i + 1][j + 1] == "M"
                and rows[i + 2][j + 2] == "A"
                and rows[i + 3][j + 3] == "S"
            ):
                # Lower right
                count += 1

print(count)
