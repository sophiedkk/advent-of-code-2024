from re import findall
from pathlib import Path

# %% Read data
data = Path("data/day_03.txt").read_text()

# %% Task 1
sum(int(d1) * int(d2) for d1, d2 in findall(r"mul\((\d+),(\d+)\)", data))

# %% Task 2
start, *rest = data.split("don't()")  # start is valid by default, so separate that from the rest
all_valid = ["".join(line.split("do()")[1:]) for line in rest]
sum(int(d1) * int(d2) for d1, d2 in findall(r"mul\((\d+),(\d+)\)", start + "".join(all_valid)))
