def selectionSort(array):
  size = len(array)
  min = 0

  for i in range(0, size - 1):
    min = i

    for j in range(i+1, size):
      if array[j] < array[min]:
        min = j

    array[min], array[i] = array[i], array[min]

  return array