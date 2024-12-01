from pathlib import Path

# %% Read data
c1, c2 = zip(*[line.split() for line in Path("data/day_01.txt").read_text().split("\n")])

# %% Task 1
sum([abs(int(value1) - int(value2)) for value1, value2 in zip(sorted(c1), sorted(c2))])

# %% Task 2
sum([int(location_id) * c2.count(location_id) for location_id in c1])
