
s = set([1, 2])
s.add(3)

s.update([1, 2])
s.update([1, 2], {1, 2})

s.remove(3)
# s.remove(4) # raise error
s.discard(4) # do nothing

len(s) # 3
s.clear()

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2 # {1, 2, 3, 4}
s1.union(s2) # {1, 2, 3, 4}
s1 & s2 # {2, 3}
s1.intersection(s2) # {2, 3}
s1 - s2 # {1}
s1.difference(s2) # {1}
s1 ^ s2 # {1, 4}
s1.symmetric_difference(s2) # {1, 4}
