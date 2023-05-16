#FIND LARGEST ELEMENT IN ARRAY: Time Complexity is theta(n) because the function will always traverse the whole array
def largestArray(arr):
  largest = 0
  for i in range(len(arr)):
    if arr[i] > largest:
      largest = arr[i]

  print('The largest element in the array is ' + str(largest))

largestArray([12, 56, 170, 66, 78, 90])