import random


def quickSort(array, l, r):
  #qs(array, l, r)
  if l<r :
    i = l
    k = random.randint(l, r)

    array[r], array[k] = array[k], array[r]

    for j in range(l, r):
      yield array, j, r, i, -1

      # if i < r:
      # j = i + 1
      # while j < r:
      if array[j] < array[r]:
        array[j], array[i] = array[i], array[j]
        i += 1

    array[i], array[r] = array[r], array[i]

    yield from quickSort(array, i + 1, r)
    yield from quickSort(array, l, i - 1)

  #return array
