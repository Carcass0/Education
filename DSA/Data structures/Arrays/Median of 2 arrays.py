import random
arr1 = [random.randint(1, 50) for i in range(15)]
arr2 = [random.randint(1, 50) for i in range(15)]
arr1 = arr1 + arr2
m1 = arr1[len(arr1)//2]
m2 = arr1[len(arr1)//2+1]
avg = (m1 + m2)/2
print(avg)