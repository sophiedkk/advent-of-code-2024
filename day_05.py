from collections import defaultdict
from pathlib import Path

# %% Load data
order, all_pages = Path("data/day_05.txt").read_text().split("\n\n")

# %% Task 1 and 2
order_dict = defaultdict(list)
for combination in [numbers.split("|") for numbers in order.splitlines()]:
    order_dict[combination[0]].append(combination[1])

correct, incorrect = [], []
for page_idx, pages in enumerate([line.split(",") for line in all_pages.splitlines()]):  # loop over all page lists
    page_scores = defaultdict(int)
    for idx, page_num in enumerate(pages):  # loop over every page in the list of pages
        for other in pages[:idx] + pages[idx+1:]:  # see how the specific page stacks up against other pages
            page_scores[page_num] += 1 if page_num in order_dict[other] else 0
    correct_order = [key for key, _ in sorted(page_scores.items(), key=lambda item: item[1])]
    if pages == correct_order:
        correct.append(int(pages[len(pages) // 2]))
    else:
        incorrect.append(int(correct_order[len(pages) // 2]))
print(f"Task 1: {sum(correct)}, Task 2: {sum(incorrect)}")
