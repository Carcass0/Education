"""Missing number from continuous integers [1, N]"""

import random

length = random.randint(10, 20)
target = [i+1 for i in range(length)]
target.remove(random.randint(1,length))
random.shuffle(target)
print(target)
helper = ['']*length
for i in target:
    helper[i-1] = i
print(helper.index('')+1)