
sorted([36, 5, -12, 9, -21]) # [ -21, -12, 5, 9, 36 ]
sorted([36, 5, -12, 9, -21], key=abs) # [ -12, 5, 9, -21, 36 ]
sorted([36, 5, -12, 9, -21], reverse=True) # [ 36, 9, 5, -12, -21 ]

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) # [ 'about', 'bob', 'Credit', 'Zoo' ]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66)]

def by_name(t):
  return t[0].lower()

def by_score(t):
  return t[1]

sorted(L, key=by_name) # [('Adam', 92), ('Bart', 66), ('Bob', 75)]
sorted(L, key=by_score, reverse=True) # [('Adam', 92), ('Bob', 75), ('Bart', 66)]