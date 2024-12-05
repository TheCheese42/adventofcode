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


def find_update_conflicts(update: list[int]) -> tuple[int, int] | None:
    for i, num in enumerate(update):
        before = update[:i]
        after = update[i + 1:]
        for other in before:
            if is_before(num, other):
                return (num, other)
        for other in after:
            if is_after(num, other):
                return (num, other)
    return None


def sort_update(update: list[int]) -> list[int]:
    print(update)
    new_update = update.copy()
    while True:
        conflicts = find_update_conflicts(new_update)
        if conflicts is None:
            break
        n1, n2 = conflicts
        i1, i2 = new_update.index(n1), new_update.index(n2)
        new_update.pop(i1)
        new_update.insert(i1, n2)
        new_update.pop(i2)
        new_update.insert(i2, n1)
    return new_update


count = 0
for update in updates:
    if find_update_conflicts(update) is not None:
        update = sort_update(update)
        count += update[(len(update) - 1) // 2]

print(count)
