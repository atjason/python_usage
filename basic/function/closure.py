def lazy_sum(*args):
  def sum():
    m = 0
    for n in args:
      m += n
    return m
  return sum # return function, but not function's result.

fn = lazy_sum(1, 2, 3)
fn() # 6, call function lazily.

def createCounter():
  n = 0
  def counter():
    nonlocal n
    n += 1
    return n
  return counter

counter = createCounter()
counter() # 1
counter() # 2
counter() # 3
