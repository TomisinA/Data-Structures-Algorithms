#MOVE ZEROES TO THE END: Time complexity is O(n)
def moveZero(arr): 
  move = 0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[i], arr[move] = arr[move], arr[i]
      move +=1

  return arr
moveZero([0, 10, 8, 0, 3, 0, 12])