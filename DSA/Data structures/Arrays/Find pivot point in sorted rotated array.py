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

if __name__=='__main__':
    import random
    import time
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    t1 = time.time()
    answer = findPivot(arr,0, len(arr))
    t2 = time.time() - t1
    print(f'answer:{answer}\ntime:{t2-t1}')