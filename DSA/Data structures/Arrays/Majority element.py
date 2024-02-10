"""Find a majority element (appears more than 0.5len times)
If one is guaranteed to exist, sort and pick the middle one.
This particular one isnt abstracted away from python but I just love Counter oh so much."""

from collections import Counter
import random

target = [random.randint(0, 2) for i in range(10)]
print(target)
l = len(target)
count = Counter(target)
if count.most_common(1)[0][1] > l/2:
    print(count.most_common(1)[0][0])
else:
    print('Нет такого')
