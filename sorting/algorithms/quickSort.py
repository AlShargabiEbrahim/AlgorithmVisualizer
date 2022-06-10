import random
def partition(array, p, r):
  i = random.randint(p, r)
  x = array[i]
  array[i] = array[r]
  i = p

  while i < r and array[i] <= x:
    i += 1

  if i < r:
    j = i + 1
    while j < r:
      if array[j] < x:
        array[i], array[j] = array[j], array[i]
        i += 1
      j += 1
  else:
    array[r] = x

  array[r] = array[i]
  array[i] = x

  return i

def qs(array, p, r):
  if p < r:
    q = partition(array, p, r)
    qs(array, p, q - 1)
    qs(array, q + 1, r)

def quickSort(array):
  size = len(array)

  qs(array, 0, size-1)

  return array