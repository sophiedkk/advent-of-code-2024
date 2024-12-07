from operator import add, mul
from pathlib import Path

data = Path("data/day_07.txt").read_text()

answers, eqs = [], []
for line in data.splitlines():
    line_answer, line_equation = line.split(": ")
    eqs.append([int(num) for num in line_equation.split(" ")])
    answers.append(int(line_answer))


def find_equation(answer, numbers, idx = 1, prev = None, ops = None) -> bool:
    if idx >= len(numbers):
        if prev == answer:
            return True
        return False

    for op in ops:
        next_value = int(f"{prev}{numbers[idx]}") if op == "||" else op(prev, numbers[idx])
        if find_equation(answer, numbers, idx + 1, next_value, ops=ops):
            return True
    return False


# %% Task 1
sum(answer if find_equation(answer, eq, prev=eq[0], ops=[add, mul]) else 0 for answer, eq in zip(answers, eqs))

# %% Task 2
sum(answer if find_equation(answer, eq, prev=eq[0], ops=[add, mul, "||"]) else 0 for answer, eq in zip(answers, eqs))
