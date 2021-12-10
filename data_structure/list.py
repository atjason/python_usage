
# enumerate
arr = ['a', 'b', 'c']
for char in arr:
  print(char)
for index, char in enumerate(arr):
  print(index, char)

# filter
arr = [0, 1, 2]
arr = [n for n in arr if n > 0]
print(arr) # [1, 2]

# map
list(map(lambda n: n * 2, [0, 1, 2])) # [0, 2, 4]
[n * 2 for n in [0, 1, 2]] # [0, 2, 4]

# copy
arr2 = arr[:]
arr2 = arr.copy()

# sort
arr = [2, 1, 3]
arr.sort() # [1, 2, 3]
arr.sort(reverse=True) # [3, 2, 1]
arr.sort(key=lambda x: -x) # [3, 2, 1]
['A', 'b', 'c'].sort(key=str.lower)

# max/min
d = [{'age': 3}, {'age': 4}]
max(d, key=lambda p: p['age'])['age'] # 4
min(d, key=lambda p: p['age'])['age'] # 3

# tips
len([1,2,3]) # 3
[1,2] + [3,4] #[1,2,3,4]
['a'] * 4 #['a', 'a', 'a', 'a']
1 in [1,2] # True

# operation
l = [1]
l.append(2) # l: [1,2]
l.extend([2,3]) # l: [1,2,2,3]
l.insert(2, 3) # l: [1,2,3,2,3]

# [].pop() # raise error
l.pop() # 3, l: [1,2,3,2]
l.count(2) # 2
l.index(2) # 1, first martched location
# l.index('a') # error if not in the list.

l.remove(2) # l: [1,3,2], remove the first matched.
# l.remove('a') # raise error if doesn't have.
l.append(4) # l: [1,3,2,4]
del l[3] # l: [1,3,2]

l.reverse() # l: [2,3,1]
l.copy() # [2,3,1]
l.clear() # l: []
