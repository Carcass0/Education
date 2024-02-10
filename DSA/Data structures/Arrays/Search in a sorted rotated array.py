import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Algorithms.Search.binsearch import binsearch
from Pivot_array import pivot_array
import random

def findPivot(arr: list, low:int, high:int) -> int:
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((low + high)//2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)

arr = [i for i in range(15)]
arr = pivot_array(arr, random.randint(3,10))
x = random.randint(0,15)
print(f'{arr}\n{x}')
pivot = findPivot(arr, 0, len(arr))
if pivot == -1:
    print(binsearch(arr, x))
    exit()
if arr[pivot] == x:
    print(arr[pivot])
    exit()
if arr[0]<=x:
    print(binsearch(arr[:pivot], x))
else:
    print(binsearch(arr[pivot+1:], x) + pivot+1)

