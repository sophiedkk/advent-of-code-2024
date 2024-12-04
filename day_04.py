from pathlib import Path

# %% Read data & setup
grid: list[list[str]] = [list(line) for line in Path("data/day_04.txt").read_text().splitlines()]
WORD: list[str] = ["X", "M", "A", "S"]


def validate_word(word: list[str], to_check: list[str]) -> bool:
    return word == to_check or word == to_check[::-1]


# %% Task 1
count = 0
for y, line in enumerate(grid):
    for x in range(len(line)):
        count += validate_word(WORD, line[x:x+len(WORD)])  # forward
        count += validate_word(WORD, [grid[y_down][x] for y_down in range(y, min(len(grid), y + len(WORD)))])  # down

        if x + len(WORD) <= len(grid[0]) and y + len(WORD) <= len(grid):  # check bounds
            count += validate_word(WORD, [grid[y+diag][x+diag] for diag in range(len(WORD))])  #diagonal right
        if x - len(WORD) + 1 >= 0 and y + len(WORD) <= len(grid):  # check bounds
            count += validate_word(WORD, [grid[y+diag][x-diag] for diag in range(len(WORD))])  # diagonal left
print(count)
