with open("01-1.txt", "r", encoding="utf-8") as fp:
    text = fp.readlines()

ids: list[list[int]] = [[], []]
for line in text:
    line = line.strip()
    if not line:
        continue
    nums = line.split("   ")
    ids[0].append(int(nums[0]))
    ids[1].append(int(nums[1]))

ids[0].sort()
ids[1].sort()
diffs: list[int] = []
for n1, n2 in zip(ids[0], ids[1]):
    diffs.append(abs(n2 - n1))

print(sum(diffs))
