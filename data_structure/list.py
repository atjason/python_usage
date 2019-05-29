
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
