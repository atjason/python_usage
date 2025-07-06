
from collections.abc import Iterable

isinstance('abc', Iterable) # True
isinstance([1, 2], Iterable) # True
isinstance((1, 2), Iterable) # True
isinstance({1, 2}, Iterable) # True
isinstance({'a': 1}, Iterable) # True

# range
for i in range(3):
  print(i) # 0, 1, 2

for i in range(5, 8):
  print(i) # 5, 6, 7

for ch in 'ABC':
  print(ch) # A, B, C

# else: only happen when loop ends normally and there's no `break` in for/while.
flag = 0
for n in [1, 2]:
  if n == 2:
    flag = 1
    break
if flag == 1:
  print('2 is found.')

for n in [1, 3]:
  if n == 2:
    break
else:
  print('2 is not found.')

a = 1
while a < 3:
  print(a, 'is small than 3.')
  a += 1
else:
  print(a, 'is same with or bigger than 3.')

for i, char in enumerate(['a', 'b']):
  print(i, char)

kv = {'a': 1, 'b': 2}

for k in kv:
  print(k, kv[k])

for k in kv.keys():
  print(k, kv[k])
  
for v in kv.values():
  print(v)

for k, v in kv.items():
  print(k, v)
