#LEFT ROTATE AN ARRAY BY D PLACES: Time Complexity is Theta(n)
#We use reversal algorithm to solve this.
def reversalAlgo(arr, low, high):
  while low < high:
    arr[low], arr[high] = arr[high], arr[low]
    low += 1
    high -= 1

def leftRotateByD(nums, d):
  n = len(nums)
  reversalAlgo(nums, 0, d-1)
  reversalAlgo(nums, d, n-1)
  reversalAlgo(nums, 0, n-1)

  return nums

leftRotateByD([12, 56, 70, 66, 78, 90], 3)