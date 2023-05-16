#CHECK IF AN ARRAY IS SORTED: Time Complexity is O(n)
def sortedArray(arr):
  for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
      print('Array is not sorted')
      return

  print('Array is sorted')

sortedArray([12, 16, 17, 66, 78, 90])