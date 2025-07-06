
def square(x):
  return x * x

map(square, range(5)) # [0, 1, 4, 9, 16]
map(lambda x: x*x, range(5)) # [0, 1, 4, 9, 16]

map(str, range(5)) # ['0', '1', '2', '3', '4']

