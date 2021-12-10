
from os import remove

filename = 'file/tmp.txt'
with open(filename, 'w') as f:
  f.write('line 1\nline 2')

with open(filename, 'r') as f:
  str = f.read() # 'line 1\nline 2'

with open(filename, 'r') as f:
  lines = []
  for line in f:
    lines.append(line)
  lines # ['line 1\n', 'line 2'], note for '\n' included.

with open(filename, 'r') as f:
  lines = f.readlines() # ['line 1\n', 'line 2'], note for '\n' included.

with open(filename, 'r') as f:
  lines = f.read().splitlines() # ['line 1', 'line 2'], note for '\n' striped.

remove(filename)