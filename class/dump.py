import json

class G:
  a = 'a'
  d = {
    'name': 'Tom',
  }
g = G()


def dump(obj):
  d = {}
  for attr in dir(obj):
    if attr[0] != '_':
      d[attr] = getattr(obj, attr)
  return json.dumps(d, indent=4)

print(dump(g))
