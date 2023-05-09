#BINARY SEARCH (ITERATIVE METHOD) Time Complexity is O(logn)
def binarySearch(num2, x):
  low = 0 #define variable for starting point
  high = len(num2) - 1 #define variable for ending point

  while low < high: #start a while loop that checks for the mid using floor division to return a whole number
    mid = (high + low) // 2

    if x == num2[mid]: #if true immediately return the found index
      return mid
    
    elif x > num2[mid]: #if true make the low after the mid by 1 and then check condition again
      low = mid + 1

    else:
      high = mid - 1 #if true make the high below the mid by 1 and then check condition again

  return -1 #do this if the while loop condition above isnt true

binarySearch([10,20,30,40,50,60,70], 5)