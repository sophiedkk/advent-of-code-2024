from dataclasses import dataclass
from pathlib import Path


# %% Task 1
disk_map = [int(num) for num in list(Path("data/day_09.txt").read_text())]
left, right, blocks = 0, len(disk_map) - 1, []
while left <= right:
    left_num: int = disk_map[left]

    if not left % 2:
        for _ in range(left_num):
            blocks.append(left // 2)
        left += 1
    else:  # gap
        right_num: int = disk_map[right]
        for _ in range(min(right_num, left_num)):
            blocks.append(right // 2)

        if left_num - right_num > 0:  # right gets fully exhausted into gaps
            right -= 2
            disk_map[left] -= right_num
        elif right_num == left_num:  #  perfect fit, shift both
            left += 1
            right -= 2
        else:
            disk_map[right] -= left_num
            left += 1

sum(idx * num for idx, num in enumerate(blocks))

# %% Task 2
@dataclass
class File:
    id_number: int
    mem_start: int
    mem_end: int

    @property
    def size(self):
        return self.mem_end - self.mem_start


disk_map = [int(num) for num in list(Path("data/day_09.txt").read_text())]

files = []
mem_idx = 0
for idx, block in enumerate(disk_map):
    if not idx % 2:
        files.append(File(idx // 2, mem_idx, mem_idx + block))
    mem_idx += block

for file in files[::-1]:  # traverse in reverse order
    mem_idx = 0
    for idx, block in enumerate(disk_map):  # check from left to right
        mem_idx += block
        if not idx % 2:  # only check the gaps
            continue
        if mem_idx > file.mem_start:  # can't place it lower, no need to look further
            break
        if file.size <= block:  # if it fits I sits!
            size = file.size
            file.mem_start = mem_idx - block
            file.mem_end = file.mem_start + size
            disk_map[idx] -= file.size  # decrease gap size
            disk_map[idx - 1] += file.size  # account for new occupied space
            break

sum(sum(memloc * file.id_number for memloc in range(file.mem_start, file.mem_end)) for file in files)
