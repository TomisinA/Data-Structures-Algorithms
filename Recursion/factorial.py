#FACTORIAL OF A NUMBER
def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n-1)

factorial(4)