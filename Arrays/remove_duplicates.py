#REMOVE DUPLICATES FROM A SORTED ARRAY: Time Complexity is O(n)
def removeDuplicate(arr):
  dup = 1
  for i in range(1, len(arr)):
    if arr[i] != arr[dup - 1]:
      arr[dup] = arr[i]
      dup += 1
  return arr

removeDuplicate([10, 10, 10, 20, 20, 20, 30, 30, 40, 40, 40, 50, 50, 50])