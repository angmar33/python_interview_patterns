def insert(array, rightIndex, value):
  j = rightIndex
  while j >= 0 and array[j] > value:
    array[j + 1] = array[j]
    j = j - 1
  array[j + 1] = value

  
def insertionSort(array):
  for i in range(1, len(array)):
    insert(array, i-1, array[i])
  return array
