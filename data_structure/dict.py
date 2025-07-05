
dict = {}
dict = {'Name': 'Tom', 'Age': 3}

dict['Name'] # 'Tom'

# dict['Sex'] # raise error.
dict.get('Sex') # None
dict.get('Sex') or 'Man' # 'Man'
dict.get('Sex', 'No value') # 'No value'

'Sex' in dict # False
dict['Sex'] = 'Man' # // Set new key, or modify existing key.
del dict['Sex']

str(dict) # "{'Name': 'Tom', 'Age': 3}"

dict.update({'Sex': 'Woman'}) # Merge 2 dict.

dict.pop('Sex') # raise error has no such key.

for k,v in dict.items():
  print(k, v)
