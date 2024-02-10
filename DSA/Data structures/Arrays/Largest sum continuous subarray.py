"""Using Kadane's algorithm."""

import random

target = [random.randint(-25, 25) for i in range(10)]
print(target)
l = len(target)
max_so_far = -100000000000
max_ending_here = 0
for i in range(l):
    max_ending_here = max_ending_here + target[i]
    if (max_ending_here > max_so_far):
        max_so_far = max_ending_here
    if max_ending_here < 0:
        max_ending_here = 0
print(max_so_far)