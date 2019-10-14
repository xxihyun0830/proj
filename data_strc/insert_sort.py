def insertion_sort(data):
    n = len(data)
    for i in range(1,n):
        val = data[i]
        j = i
        while j>0 and data[j-1] > val:
            data[j] = data[j-1]
            j -= 1
        data[j] = val
    return data

