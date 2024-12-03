from math import copysign as csign
from pathlib import Path

# %% Read data
reports = [[int(level) for level in levels.split()] for levels in Path("data/day_02.txt").read_text().split("\n")]
cdir = lambda numbers: all(csign(1, x) == csign(1, numbers[0]) for x in numbers)
cdif = lambda numbers: all(0 < abs(num) < 4 for num in numbers)

# %% Task 1
sum(1 for r in reports if cdif([n2 - n1 for n1, n2 in zip(r, r[1:])]) and cdir([n2 - n1 for n1, n2 in zip(r, r[1:])]))

# %%
nreports = 0
for report in reports:
    for i in range(len(report)):
        option = report[:i] + report[i+1:]
        diff = [num2 - num1 for num1, num2 in zip(option, option[1:])]
        if cdif(diff) and cdir(diff):
            nreports += 1
            break
print(nreports)
