
def __heapify(data, n, i):
    while True:
        left, right = 2*i+1, 2*i+2
        if right >= n or data[left] > data[right]:
            child = left
        else:
            child = right
        if child >= n or data[i] > data[child]:
            return
        data[i], data[child] = data[child], data[i]
        i = child

def heap_sort(data):
    n = len(data)
    for i in range(n, -1, -1):
        __heapify(data, n, i)

    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        __heapify(data, i, 0)
    return data
