with open("09-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read().strip()

files: list[str] = []

is_file = True
next_id = 0
for digit in text:
    if is_file:
        files.extend([f"{next_id}"] * int(digit))
        next_id += 1
    else:
        files.extend(["."] * int(digit))
    is_file = not is_file

for id in list(reversed(files)).copy():
    print("Processing id", id)
    if id == ".":
        continue
    start = files.index(id)
    end = max(loc for loc, val in enumerate(files) if val == id)
    length = end - start + 1
    for i, gap in enumerate(files):
        if gap != ".":
            continue
        gap_start = i
        gap_end = i
        if gap_start > start:
            continue
        while len(files) > gap_end + 1 and files[gap_end + 1] == ".":
            gap_end += 1
        gap_length = gap_end - gap_start + 1
        if gap_length >= length:
            for index in range(gap_start, gap_start + length):
                files.pop(index)
                files.insert(index, id)
            for index in range(start, end + 1):
                files.pop(index)
                files.insert(index, ".")
            break

checksum = 0
for i, id in enumerate(files):
    if id == ".":
        continue
    checksum += i * int(id)

print(checksum)
