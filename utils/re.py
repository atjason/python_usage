# https://docs.python.org/3/library/re.html

# Regular Expression Syntax
# https://docs.python.org/3/library/re.html#regular-expression-syntax

import re

# match: check the beginning.
# search: check the whole string.
# findall: check the whole string and find all matched results.

# match
re.match('jason', 'www.atjason.com') # None
re.match('www', 'www.atjason.com').span() # (0, 3)
re.match('(a)(b)', 'ab').groups() # ('a', 'b')
re.match('(a)(b)', 'ab').group() # 'ab'
re.match('(a)(b)', 'ab').group(0) # 'ab'
re.match('(a)(b)', 'ab').group(1) # 'a'
re.match('(a)(b)', 'ab').group(2) # 'b'

# search
re.search('jason', 'www.atjason.com').span() # (6, 11)

# findall
re.search('a', 'www.atjason.com') # ['a', 'a']
re.search('jason', 'www.atjason.com') # ['jason']
re.search('jason2', 'www.atjason.com') # []

# finditer
it = re.finditer(r'\d+', '12ab34cd56ef')
for match in it:
  print(match.group()) # 12, 34, 56

# split
re.split(r'\W+', 'Hello World') # ['Hello', 'World']

# sub
phone = "2004-959-559 # 这是一个国外电话号码"
phone = re.sub(r' +#.*$', '', phone) # '2004-959-559'
phone = re.sub(r'\D', '', phone) # '2004959559'

# flags
# re.I 忽略大小写
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）

# demo
s = '<img src="1.jpg">'
re.search(r'(?<=src=").*(?=">)', s).group() # '1.jpg'