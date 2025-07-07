
def is_odd(n):
  return n % 2 == 1

list(filter(is_odd, range(5))) # [1, 3]
list(filter(lambda n: n % 2 == 1, range(5))) # [1, 3]
