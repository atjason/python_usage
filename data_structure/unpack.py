
p = (4, 5)
x, y = p
x # 4
y # 5

stock_info = ['AMZN', (1810, 3), '20190531T12:38:58Z']
symbol, (price, size), _ = stock_info
symbol # 'AMZN'

arr = [1, 2, 3, 4, 5]
first, *middle, last = arr
first # 1
middle # [2, 3, 4]
last # 5

records = [
  ('foo', 1, 2),
  ('bar', 'hello'),
  ('foo', 3, 4),
]

def do_foo(x, y):
  print('foo', x, y)

def do_bar(s):
  print('bar', s)

for tag, *args in records: # pack args to list
  if tag == 'foo':
    do_foo(*args) # unpack list to params
  elif tag == 'bar':
    do_bar(*args) # unpack list to params