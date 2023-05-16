#SEARCHING AN ELEMENT IN AN ARRAY (Time complexity of O(n))
def arraySearch(arr, num):
  for i in range(len(arr)):
    if arr[i] == num:
      print('Element ' + str(num) + ' found at index ' + str(i))
      return 
  print('-1')

arraySearch([2, 23, 4, 7, 9], 9)