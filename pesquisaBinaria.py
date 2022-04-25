import random


def createRandomArray():
    res = random.sample(range(1, 100), 30)
    return res


def binary_search(arr1, target, low= None, high=None):
    mid = (len(arr1))/2
    if low == None:
        low = 0
    if high == None:
        high = len(arr1)-1    
    mid = (low+high)//2
    if arr1[mid] == target:
        return mid
    elif target < arr1[mid]:
        return binary_search(arr1, target, low, mid-1)
    else:
        return binary_search(arr1, target, mid+1, high)


arr1 = createRandomArray()
arr1 = sorted(arr1)
target = arr1[random.randint(0, 29)]
binary_search(arr1, target)








