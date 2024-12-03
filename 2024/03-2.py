import re

with open("03-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

PATTERN_DO = r"do\(\)"
PATTERN_DONT = r"don't\(\)"
dos: list[int] = []
donts: list[int] = []
for match in re.finditer(PATTERN_DO, text):
    dos.append(match.start())
for match in re.finditer(PATTERN_DONT, text):
    donts.append(match.start())

PATTERN = r"mul\((\d\d?\d?),(\d\d?\d?)\)"
result = 0
for match in re.finditer(PATTERN, text):
    last_cond = 0
    last_is_dont = False
    for do in dos:
        if match.start() > do > last_cond:
            last_cond = do
            last_is_dont = False
    for dont in donts:
        if match.start() > dont > last_cond:
            last_cond = dont
            last_is_dont = True
    if not last_is_dont:
        result += int(match.group(1)) * int(match.group(2))

print(result)
