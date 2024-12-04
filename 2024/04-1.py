import re


def find_horizontal(text: str) -> int:
    return len(re.findall("XMAS", text)) + len(re.findall("SAMX", text))


def find_vertical(text: str) -> int:
    hor_list: list[str] = text.splitlines()
    ver_list: list[str] = []
    for i in range(len(hor_list)):
        col: list[str] = []
        for row in hor_list:
            try:
                col.append(row[i])
            except IndexError:
                pass
        ver_list.append("".join(col))
    return find_horizontal("\n".join(ver_list))


def find_diagonal(text: str) -> int:
    count = 0
    lines = text.splitlines()
    # lr
    new_lines = lines.copy()
    for i, line in enumerate(lines):
        if "M" in line:
            new_lines[i] = new_lines[i][1:]
        if "A" in line:
            new_lines[i] = new_lines[i][2:]
        if "S" in line:
            new_lines[i] = new_lines[i][3:]
    count += find_vertical("\n".join(new_lines))
    # ll
    new_lines = lines.copy()
    for i, line in enumerate(lines):
        if "M" in line:
            new_lines[i] = "." + new_lines[i]
        if "A" in line:
            new_lines[i] = ".." + new_lines[i]
        if "S" in line:
            new_lines[i] = "..." + new_lines[i]
    count += find_vertical("\n".join(new_lines))
    # ur
    new_lines = lines.copy()
    for i, line in enumerate(lines):
        if "A" in line:
            new_lines[i] = new_lines[i][1:]
        if "M" in line:
            new_lines[i] = new_lines[i][2:]
        if "X" in line:
            new_lines[i] = new_lines[i][3:]
    count += find_vertical("\n".join(new_lines))
    # ul
    new_lines = lines.copy()
    for i, line in enumerate(lines):
        if "A" in line:
            new_lines[i] = "." + new_lines[i]
        if "M" in line:
            new_lines[i] = ".." + new_lines[i]
        if "X" in line:
            new_lines[i] = "..." + new_lines[i]
    count += find_vertical("\n".join(new_lines))
    return count


with open("04-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

print(find_horizontal(text) + find_vertical(text) + find_diagonal(text))
