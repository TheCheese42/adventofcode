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

counts: list[int] = []
for n in ids[0]:
    counts.append(n * ids[1].count(n))

print(sum(counts))
