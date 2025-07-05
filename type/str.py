# str: https://docs.python.org/3/library/stdtypes.html
# string: https://docs.python.org/3/library/string.html

# capitalize/title
'hello'.capitalize() # 'Hello'
'hello world'.title() # 'Hello World'.

# start/end
'ab'.startswith('a') # True
'ab'.endswith('b') # True

# in/find/rfind/index/rindex/replace/count
'a' in 'ab' # True
'ab'.find('a') # 0
'ab'.find('b') # 1
'ab'.find('c') # -1
'ab'.index('a') # 0
'ab'.count('a') # 1
'ab'.replace('a', 'c') # 'cb'

# join
', '.join(['1', '2']) # '1, 2'
', '.join(map(str, [1, 2])) # '1, 2'

# center/ljust/rjust/zfill
'a'.center(3) # ' a '
'a'.center(3, '-') # '-a-'
'a'.ljust(3) # 'a  '
'a'.rjust(3) # '  a'
'42'.zfill(5) # '00042'
'-42'.zfill(5) # '-0042'

# strip/lstrip/rstrip
' a'.strip() # 'a'
'abcd'.strip('dcba') # '' Note: all chars removed, but not just prefix/suffix.

# split/splitlines/partition/rpartitioin
'a,b,c'.split(',') # ['a', 'b', 'c']
'a,b,c'.partition(',') # ('a', ',', 'b,c')

# isdigit/isnumeric/isdecimal
# isdecimal() ⊆ isdigit() ⊆ isnumeric()
# +-------------+-----------+-------------+----------------------------------+
# | isdecimal() | isdigit() | isnumeric() |          Example                 |
# +-------------+-----------+-------------+----------------------------------+
# |    True     |    True   |    True     | "038", "੦੩੮", "０３８"            |
# |   False     |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧", "2²"    |
# |   False     |   False   |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "一貳參" |
# |   False     |   False   |   False     | "abc", "38.0", "-38"             |
# +-------------+-----------+-------------+----------------------------------+

# format
# https://docs.python.org/3/library/string.html#formatstrings
str.format('{}', 1)
'{}'.format(1)
f'{1}'

name = 'Tom'
f'Hello {name}' # 'Hello Tom'

# Accessing arguments by position:
'{0}, {1}, {2}'.format('a', 'b', 'c') #'a, b, c'
'{}, {}, {}'.format('a', 'b', 'c')  # 'a, b, c'
'{2}, {1}, {0}'.format('a', 'b', 'c') #'c, b, a'
'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence, 'c, b, a'
'{0}{1}{0}'.format('a', 'b')   # arguments' indices can be repeated, 'aba'

# Accessing arguments by name:
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W') # 'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord) # 'Coordinates: 37.24N, -115.81W'

# Accessing arguments’ items:
'X: {0[0]};  Y: {0[1]}'.format((3, 5)) # 'X: 3;  Y: 5'

# % Formatting with % operator:
'Hi %s, your score is %d' % ('Tom', 82)
# 'Hi Tom, your score is 82'
'%2d-%02d' % (3, 1)
# ' 3-01'
'%.1f' % 3.1415926
# '3.14'
'%.1f%%' % 18.23
# '18.2%'

# Replacing %s and %r:
"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
# "repr() shows quotes: 'test1'; str() doesn't: test2"

# Aligning the text and specifying a width:
'{:<30}'.format('left aligned')
# 'left aligned                  '
'{:>30}'.format('right aligned')
# '                 right aligned'
'{:^30}'.format('centered')
# '           centered           '
'{:*^30}'.format('centered')  # use '*' as a fill char

'{:2d}'.format(1) # ' 1'
'***********centered***********'

# Replacing %+f, %-f, and % f and specifying a sign:
'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
# '+3.140000; -3.140000'
'{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
# ' 3.140000; -3.140000'
'{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
# '3.140000; -3.140000'

# Using the comma as a thousands separator:
'{:,}'.format(1234567890) # '1,234,567,890'

# Expressing a percentage:
'Correct answers: {:.2%}'.format(19/22) # 'Correct answers: 86.36%'
'Correct answers: {:.2f}'.format(19/22) # 'Correct answers: 0.86'

# Using type-specific formatting:
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(d) # '2010-07-04 12:15:58'
