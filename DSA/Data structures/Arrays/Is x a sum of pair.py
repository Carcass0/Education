"""See if a given number is a sum of 2 other numbers in an array"""

import random

target = [random.randint(0, 25) for i in range(10)]
l = len(target)
answer = False
x = random.randint(7,37)
for i in range(l):
    for j in range(i+1, l):
        if target[i] + target[j] == x:
            answer = True
print(f'{target}\n{x}\n{answer}')
