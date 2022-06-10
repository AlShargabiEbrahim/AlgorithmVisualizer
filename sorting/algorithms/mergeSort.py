def mergeSort(A, *args):
    n = len(A)
    B = [0 for i in range(n)]
    for i in range(0, n):
        B[i] = A[i]

    ms(B, A, 0, n)

    return A


def ms(B, A, l, r):
    if r - l > 1:
        m = l + (r - l) // 2
        ms(A, B, l, m)
        ms(A, B, m, r)
        merge(B, A, l, m, r)


def merge(B, A, l, m, r):
    i = k = l
    j = m

    while i < m and j < r:
        if B[i] <= B[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = B[j]
            j = j + 1
        k = k + 1

    if i < m:
        for l in range(k, r):
            A[l] = B[i]
            i = i + 1
    else:
        for l in range(k, r):
            A[l] = B[j]
            j = j + 1
