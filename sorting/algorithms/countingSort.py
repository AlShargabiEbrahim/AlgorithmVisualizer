def countingSort(array, *args):
    # no duplicates are allowed
    size = len(array)
    countArr = [0]*(max(array)+1)
    output =array.copy()

    for i in range(0, size):
        countArr[array[i]] += 1

    for k in range(1, len(countArr)):
        countArr[k] += countArr[k - 1]

    for i in range(0, size):
        yield array, countArr[output[size - i - 1]] - 1, -1, size - i - 1, -1
        array[countArr[output[size - i - 1]] - 1] = output[size - i - 1]
        countArr[output[size - i - 1]] -= 1

    #for k in range(0, len(array) - 1):
        #array[k] = output[k]

    #return output


"""
def countingSort(array, *args):
    # no duplicates are allowed
    size = len(array)
    countArr = [0]*(max(array)+1)
    output = [array[i] for i in range(size)]

    for i in range(size):
        countArr[output[i]] += 1

    for k in range(1, len(countArr)):
        countArr[k] += countArr[k - 1]

    #j = size - 1
    #while j >= 0:
    for i in range(0,size):
        yield array, countArr[output[size - i - 1]] - 1, -1, size - i - 1, -1
        array[countArr[output[size-i-1] ]- 1] = output[size-i-1]
        countArr[output[size-i-1]] -= 1
       ## j -= 1
    """