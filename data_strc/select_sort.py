
def selection_sort(data):
    n = len(data)
    for i in range(n):
        smallest = data[i]
        smallest_idx = i
        for j in range(i,n):
            if smallest > data[j]:
                smallest = data[j]
                smallest_idx = j
        if i != smallest_idx:
            data[i], data[smallest_idx] = data[smallest_idx], data[i]
    return data