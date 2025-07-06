
g = (x * x for x in range(1, 11))

for i in g:
  print(i)  # 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n += 1

for n in fib(5):
  print(n)  # 0, 1, 1, 2, 3

