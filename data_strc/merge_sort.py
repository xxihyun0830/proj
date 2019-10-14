
def merge_sort(data):
    __merge_sort(data, 0, len(data)- 1)
    return data

def __merge_sort(data, left, right):
    if left >= right:
        return
    m = int((left+right)/2)
    __merge_sort(data, left, m)
    __merge_sort(data, m+1, right)
    __merge(data, left, m, right)

def __merge(data, left, middle, right):
    a = data[left:middle+1]
    b = data[middle+1:right+1]
    i = 0
    j = 0 
    k = left
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            data[k] = a[i]
            i += 1
        else:
            data[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        data[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        data[k] = b[j]
        j += 1
        k += 1