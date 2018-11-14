class MathDojo:
  def __init__(self):
    self.result = 0
  def add(self, *num):
    for i in range(0, len(num)):
      self.result += num[i]
    return self
  def subtract(self, *num):
    for i in range(0, len(num)):
      self.result -= num[i]
    return self
  def output(self):
    print(self.result)
    
md=MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).output()
print(x)

