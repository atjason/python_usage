
score = 'B'

# Match statements require Python 3.10 or newer
match score:
  case 'A':
    print('Excellent!')
  case 'B':
    print('Good job!')
  case 'C':
    print('You can do better.')
  case _:
    print('Invalid score.')

age = 15

match age:
  case x if x < 10:
    print(f'< 10 years old: {x}')
  case 10:
    print('10 years old')
  case 11 | 12 | 13:
    print('11, 12, or 13 years old')
  case _:
    print(f'Older than 13 years old: {age}')

args = ['gcc', 'hello.c', 'world.c']

match args:
  case ['gcc']:
    print('gcc: missing source file(s).')
  case ['gcc', file1, *files]:
    print('gcc compile: ' + file1 + ', ' + ', '.join(files))
  case _:
    print('Invalid command.')
    