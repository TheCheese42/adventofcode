with open("09-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read().strip()

files: list[str] = []
gaps: list[tuple[int, int]] = []  # (pos, blocks)

is_file = True
next_id = 0
for digit in text:
    if is_file:
        files.extend([f"{next_id}"] * int(digit))
        next_id += 1
    else:
        gaps.append((len(files), int(digit)))
    is_file = not is_file

blocks_inserted = 0
while gaps:
    pos, blocks = gaps.pop(0)
    for _ in range(blocks):
        id = files.pop()
        files.insert(pos + blocks_inserted, id)
        pos += 1
    blocks_inserted += blocks

checksum = 0
for i, id in enumerate(files):
    checksum += i * int(id)
print(checksum)
