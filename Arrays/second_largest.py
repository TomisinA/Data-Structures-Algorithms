#SECOND LARGEST ELEMENT IN ARRAY: Time Complexity is Theta(n)
def secondLargest(arr):
  largest = 0
  second_largest = 0
  for i in range(len(arr)):
    if arr[i] > largest:
      second_largest = largest
      largest = arr[i]
    elif arr[i] < largest and arr[i] > second_largest:
      second_largest = arr[i]
      
  print('The second largest is ' +str(second_largest))

secondLargest([12, 56, 70, 66, 78, 90])