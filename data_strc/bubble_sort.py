
def bubble_sort(data):
    n = len(data)
    for i in range(n-1, 0, -1):
        for j in range(0,i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data