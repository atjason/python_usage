import pandas as pd

# Series

a = ['a', 'b', 'c']
var = pd.Series(a)
print(var[1]) # 'b'

a = ['Apple', 'Google', 'Microsoft']
var = pd.Series(a, index=['A', 'G', 'M'])
print(var['G']) # 'Google'

d = {'A': 'Apple', 'G': 'Google', 'M': 'Microsoft'}
var = pd.Series(d)
print(var['G']) # 'Google'

# DataFrame
