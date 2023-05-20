#PRINT N TO 1 USING RECURSION: O(n) auxilliary space
def Nto1_Recursion(n):
  if n == 0:
    return

  print(n)
  Nto1_Recursion(n-1)

Nto1_Recursion(5)