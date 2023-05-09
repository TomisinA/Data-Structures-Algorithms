#BINARY SEARCH (RECURSIVE METHOD) Time complexity is O(log n) and space complexity is O(log n) because recursive functions need to be stored in stack temporarily
def binarySearch(num2, low, high, x):

  if low <= high: #start an if condition loop and compute the mid using floor division to return a whole number
    mid = (high + low) // 2

    if x == num2[mid]: #if true immediately return the found index
      return mid
    
    elif x > num2[mid]: #if true, return a recursive call where low becomes an increase of mid by 1
      return binarySearch(num2, mid+1, high, x)

    else:
      return binarySearch(num2, low, mid-1, x) #if true, return a recursive call where high becomes a decrease of mid by 1

  else:
    return -1 #do this if the if condition above isnt true
num2 = [10,20,30,40,50,60,70]
binarySearch(num2, 0, len(num2) -1, 5)