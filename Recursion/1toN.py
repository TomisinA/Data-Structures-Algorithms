#PRINT 1 TO N USING RECURSION: O(n) auxilliary space
def OnetoN_Recursion(n):
  if n == 0:
    return 

  OnetoN_Recursion(n-1)
  print(n)

OnetoN_Recursion(5)