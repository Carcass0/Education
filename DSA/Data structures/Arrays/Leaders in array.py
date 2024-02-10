"""A leader is an item greater than all items to its left"""

import random

target = [random.randint(0, 25) for i in range(10)]
l = len(target)-1
answer = []
for i in range(l+1):
    flag = False
    for j in range(i+1, l+1):
        if target[j] >= target[i]:
            break
        elif j==l:
            flag = True
    if flag: answer.append(target[i])
print(target, '\n', answer)
