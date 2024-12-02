with open("02-1.txt", "r", encoding="utf-8") as fp:
    text = fp.readlines()

num_safe = 0
for report in text:
    report = report.strip()
    nums = [int(i) for i in report.split(" ")]
    if nums[0] < nums[1]:
        inc = True
    else:
        inc = False
    prev = None
    report_safe = True
    for num in nums:
        if prev is not None:
            if inc:
                if not (1 <= (num - prev) <= 3):
                    report_safe = False
            else:
                if not (1 <= (prev - num) <= 3):
                    report_safe = False
        prev = num
    if report_safe:
        num_safe += 1

print(num_safe)

