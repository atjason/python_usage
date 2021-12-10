
l = [1, 2]
it = iter(l)
for i in it:
  print(i) # 1, 2

print()

# iterator class

class MyNumber():

  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a < 3:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

num = MyNumber()
for n in iter(num):
  print(n) # 1, 2

print()

# generator: function with yield

def iterN(n):
  i = 1
  while True:
    if i > n:
      return
    yield i
    i += 1

for i in iterN(2):
  print(i)
