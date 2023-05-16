#DELETE AN ELEMENT IN AN ARRAY: Time Complexity is O(n)
def deleteArray(arr, num):
  for i in range(len(arr)):
    if arr[i] == num:
      break
  while i < len(arr)-1:
    arr[i] = arr[i+1]
    i += 1
  arr[-1] = None
  print(arr)

deleteArray([12, 56, 70, 66, 78], 56)