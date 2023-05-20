#SUM OF N NATURAL NUMBERS: Time Complexity and Space Complexity is Theta(n)
def sumNatural(n):
  if n <= 1:
    return n

  return n + sumNatural(n-1)

sumNatural(4)