from random import randint
from datetime import *

array = [randint(1, 10000) for i in range(100000000)]
array.sort()


def binSearch(arr, key):

    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    while arr[mid] != key and low <= high:
        mid = (low + high) // 2

        if key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1


def linearSearch(arr, key):
    search = 0
    found = False

    while search < len(arr) and found is False:
        if arr[search] == key:
            found = True
        else:
            search += 1

        return found


start = datetime.now()
linearSearch(array, randint(1, 10000))
finish = datetime.now() - start

print(finish)

start = datetime.now()
binSearch(array, randint(1, 10000))
finish = datetime.now() - start
print(finish)
