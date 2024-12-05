with open("05-1.txt", "r", encoding="utf-8") as fp:
    text = fp.read()

raw_rules: list[str] = text.split("\n\n")[0].splitlines()
rules: list[tuple[int, int]] = []
for raw_rule in raw_rules:
    r1, r2 = raw_rule.split("|")
    rules.append((int(r1), int(r2)))

raw_updates: list[str] = text.split("\n\n")[1].splitlines()
updates: list[list[int]] = [list(map(int, i.split(","))) for i in raw_updates]


def is_before(n1: int, n2: int) -> bool:
    for rule in rules:
        if n1 == rule[0] and n2 == rule[1]:
            return True
    return False


def is_after(n1: int, n2: int) -> bool:
    for rule in rules:
        if n1 == rule[1] and n2 == rule[0]:
            return True
    return False


def is_update_correct(update: list[int]) -> bool:
    for i, num in enumerate(update):
        before = update[:i]
        after = update[i + 1:]
        for other in before:
            if is_before(num, other):
                return False
        for other in after:
            if is_after(num, other):
                return False
    return True


count = 0
for update in updates:
    if is_update_correct(update):
        count += update[(len(update) - 1) // 2]

print(count)
