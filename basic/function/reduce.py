from functools import reduce

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
  return x + y

reduce(add, [1, 2, 3, 4]) # 10

def fn(x, y):
  return x * 10 + y

reduce(fn, [1, 2, 3, 4]) # 1234
