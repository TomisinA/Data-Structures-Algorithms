#Stack Implementation in Python using List

class Stack():
  def __init__(self, size):
    self.size = size
    self.stack = []
    

  def push(self, n):
    if len(self.stack) < self.size:
      self.stack.append(n)
      print(self.stack)
    else:
      print('Stack Overflow')
    
  def pop(self):
    if self.stack:
      self.stack.pop()
      print(self.stack)
    else:
      print('Stack Underflow')

  def peek(self):
    if self.stack:
      print(self.stack[-1])
    else:
      print('Stack Underflow')

  def isEmpty(self):
    if self.stack:
      return False
    else:
      return True

S1 = Stack(5)