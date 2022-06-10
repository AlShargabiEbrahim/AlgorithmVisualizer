def selectionSort(array, *args):
  size = len(array)
  min = 0

  for i in range(0, size - 1):
    min = i

    for j in range(i+1, size):
      yield array, j, -1, i, -1
      if array[j] < array[min]:
        min = j

    array[min], array[i] = array[i], array[min]

  #return array