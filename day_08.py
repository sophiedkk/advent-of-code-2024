from collections import defaultdict
from pathlib import Path

# %% Read data
grid = [list(line) for line in Path("data/day_08.txt").read_text().splitlines()]

# %% Part 1 & part 2
antennas = defaultdict(list)
[antennas[val].append((x, y)) for y, row in enumerate(grid) for x, val in enumerate(row) if val != "."]

antinodes, harmonics = set(), set()
for locations in antennas.values():
    if len(locations) > 1:
        harmonics |= set(locations)
    for idx, loc in enumerate(locations):
        for other in locations[:idx] + locations[idx + 1:]:
            harmonic = 0
            while (0 <= (antinode_x := loc[0] + (loc[0] - other[0]) * (harmonic + 1)) < len(grid[0])
                   and 0 <= (antinode_y := loc[1] + (loc[1] - other[1]) * (harmonic + 1)) < len(grid)):
                if harmonic:
                    harmonics.add((antinode_x, antinode_y))
                else:  # Base harmonic, part of exercise 1
                    antinodes.add((antinode_x, antinode_y))
                harmonic += 1
print(f"Answer part 1: {len(antinodes)}, answer part 2: {len(antinodes | harmonics)}")

