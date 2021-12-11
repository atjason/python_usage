# https://docs.python.org/3/library/json.html

import os
import json

j = {'name': 'Tom', 'age': 3}
j_str = json.dumps(j) # '{"name": "Tom", "age": 3}'
json.loads(j_str) # {'name': 'Tom', 'age': 3}

path = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(path, 'json_file.json')
  
with open(filepath, 'w') as f:
  json.dump(j, f, indent=2)

with open(filepath) as f:
  j = json.load(f)