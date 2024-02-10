from typing import Iterable


def binsearch[T](victim: Iterable[T], target: T, length: int = 0) -> int:
    """Binary search. Returns -1 if target isn't found."""
    def get_middle(start: int, end:int) -> int:
        return start + (end - start)//2

    left_end = 0
    if length:
        right_end = length-1
    else:
        right_end = len(victim)-1
    while True:
        if victim[left_end] == target:
            return left_end
        if victim[right_end] == target:
            return right_end
        mid = get_middle(left_end, right_end)
        if victim[mid] == target:
            return mid
        if target>victim[mid]:
            left_end = mid + 1
        else:
            right_end = mid - 1
        if right_end <= left_end:
            if victim[right_end] == target:
                return right_end
            else:
                return -1

def binarySearch(arr, low, high, key):
 
    if high < low:
        return -1
 
    # low + (high - low)/2;
    mid = int((low + high)/2)
 
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                            key)
    return binarySearch(arr, low, (mid - 1), key)

if __name__=='__main__':
    import random
    import time
    arr = [random.randint(-1250, 1250) for i in range(100_000_000)]
    arr.sort()
    x = random.randint(-1250, 1250)
    t1 = time.time()
    answer = binsearch(arr, x)
    t2 = time.time() - t1
    print(f'answer:{answer}\ntime:{t2-t1}')
    t1 = time.time()
    answer = binarySearch(arr, 0, len(arr), x)
    t2 = time.time() - t1
    print(f'answer:{answer}\ntime:{t2-t1}')