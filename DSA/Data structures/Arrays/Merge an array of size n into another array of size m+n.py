"""Both arrays are sorted."""
import random
from Pivot_array import pivot_array

n = 15
m = 10
big_arr = [random.randint(1, 50) for i in range(n)]
big_arr = sorted(big_arr)
for i in range(m):
    big_arr.append(0)
big_arr = pivot_array(big_arr, 15)
print(big_arr)
small_arr = [random.randint(1,50) for i in range(n)]
small_arr = sorted(small_arr)
print(small_arr)
i = n #point at which the values in bigger start
j = 0 #cycle through smaller
k = 0 #cycle through output
while(k < m+n):
    if ((j == n) or (i < (m + n) and big_arr[i] <= small_arr[j])):
        big_arr[k] = big_arr[i]
        k += 1
        i += 1
    else:
        big_arr[k] = small_arr[j]
        k += 1
        j += 1
print(big_arr)