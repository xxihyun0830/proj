
import random
def __partition(data, left, right):
    r = random.randint(left, right)
    data[left], data[r] = data[r], data[left]
    pivot = left
    store = left + 1
    for i in range(left+1, right +1):
        if data[i] < data[pivot]:
            data[i], data[store] = data[store], data[i]
            store += 1
    data[pivot], data[store - 1] = data[store - 1], data[pivot]
    return store -1

def __quick_sort(data, left, right):
    if left >= right:
        return
    pivot = __partition(data, left, right)
    __quick_sort(data, left, pivot-1)
    __quick_sort(data, pivot+1, right)

def quick_sort(data):
    __quick_sort(data, 0, len(data)- 1)
    return data