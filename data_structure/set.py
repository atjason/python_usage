
s = set([1, 2])
s.add(3)

s.update([1, 2])
s.update([1, 2], {1, 2})

s.remove(3)
# s.remove(4) # raise error
s.discard(4) # do nothing

len(s) # 3
s.clear()
