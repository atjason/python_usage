
if True:
  msg = 1
print(msg) # Could access varaible defined in if/elif/else/, try/except, for/while.

num = 1
def f1():
  global num # Could access without `global`, but can't modify without it.
  num = 2
  print(num)
f1()
print(num)

def outer():
  num = 10
  def inner():
    nonlocal num # Note: `nolocal`, similar with `global`.
    num = 100
    print(num)
  inner()
  print(num)
outer()
