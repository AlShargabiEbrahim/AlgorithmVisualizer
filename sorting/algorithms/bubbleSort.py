def bubbleSort(array):
  size = len(array)

  for i in range (size):

    for j in range(0, size-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]

  return array