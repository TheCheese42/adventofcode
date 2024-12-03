import re

with open("03-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

PATTERN = r"mul\((\d\d?\d?),(\d\d?\d?)\)"
result = 0
for match in re.findall(PATTERN, text):
    if match:
        result += int(match[0]) * int(match[1])

print(result)
