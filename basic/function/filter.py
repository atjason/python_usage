
def is_odd(n):
  return n % 2 == 1

list(filter(is_odd, range(10))) # [1, 3, 5, 7, 9]

def not_empty(s):
  return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])) # ['A', 'B', 'C']
