#LEFT ROTATE AN ARRAY BY 1: Time Complexity is Theta(n)
def leftRotate(nums):
  last = nums[0]
  for i in range(1, len(nums)):
    nums[i-1] = nums[i]
  nums[-1] = last
  return nums

leftRotate([12, 56, 70, 66, 78, 90])