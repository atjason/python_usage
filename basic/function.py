
def max(a, b):
  if a > b:
    return a
  else:
    return b

max(1, 2) # 2

# param name.

def f1(name, age):
  print(name, age)

f1(age=3, name='Tom')

# param default value.

def f2(name, age=3):
  print(name, age)

f2('Jim')

# variable params.

def f3(*args):
  for arg in args:
    print(arg)

f3(1, 2, 3)

def f4(**args_dict):
  for k,v in args_dict.items():
    print(k, v)

f4(name='Tom', age=3)

# lambda

sum = lambda a, b: a + b

sum(1, 2) # 3
