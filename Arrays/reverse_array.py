#REVERSE AN ARRAY: Time Complexity is Theta(n)
def reverseArray(arr):
  low = 0
  high = len(arr) -1
  temp = 0
  if len(arr) == 1:
    return arr #immediately return the array if there is only one element
  
  while low <= high:
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp
    low += 1
    high -= 1

  print(arr)

reverseArray([12, 56, 70, 66, 78, 90])