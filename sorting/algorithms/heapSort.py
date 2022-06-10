def heapify(array, cnt):
    s = (cnt - 1) // 2
    while s >= 0:
        yield from sd(array, s, cnt - 1)
        s -= 1


def heapSort(arr, *args):
    n = len(arr)
    yield from heapify(arr, n)
    k = len(arr) - 1
    while k > 0:
        yield arr, -1, -1, 0, k
        arr[k], arr[0] = arr[0], arr[k]
        k -= 1
        yield from sd(arr, 0, k)
    #return arr


def sd(array, s, e):

    r = s
    while 2 * r + 1 <= e:
        c = 2 * r + 1
        swap = r
        
        if array[swap] < array[c]:
            swap = c
            
        if c + 1 <= e and array[swap] < array[c + 1]:
            swap = c + 1
            
        if swap == r:
            return
        
        else:
            yield array, r, swap, -1, -1
            array[r], array[swap] = array[swap], array[r]
            r = swap