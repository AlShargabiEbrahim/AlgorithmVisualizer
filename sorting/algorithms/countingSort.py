def countingSort(array):
    # no duplicates are allowed
    size = len(array)
    countArr = [0 for i in range(256)]
    output = [0 for i in range(size)]

    for i in range(0, size):
        countArr[array[i]] += 1

    for k in range(0, 256):
        countArr[k] += countArr[k - 1]

    j = size - 1
    while j >= 0:
        output[countArr[array[j] - 1]] = array[j]
        countArr[array[j]] -= 1
        j -= 1

    for k in range(0, len(array) - 1):
        array[k] = output[k]

    return output
