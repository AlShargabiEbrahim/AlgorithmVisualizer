def mergeSort(A, l , r):
    n = len(A)
    B = [0 for i in range(n)]
    if r > l:
        m = int((l+r)/2)
        yield from mergeSort(A, l, m)
        yield from mergeSort(A, m + 1, r)
        yield from merge(B,A, l, m, r)


def merge(B, A, l, m, r):
    left_arr = A[l:m + 1]
    right_arr = A[m + 1:r + 1]
    i = 0
    j = 0
    k = l
    
    while i < len(left_arr) and j < len(right_arr):
        yield A, l + i, m + j, l, r
        
        if left_arr[i] < right_arr[j]:
            A[k] = left_arr[i]
            i += 1
        else:
            A[k] = right_arr[j]
            j += 1
            
        k += 1

    while i < len(left_arr):
        A[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        A[k] = right_arr[j]
        j += 1
        k += 1