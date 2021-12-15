
# 1. SimpleNamespace
from types import SimpleNamespace

dummy_object = SimpleNamespace(a=1)

# Creation of attributes
dummy_object.name = 'dummy_name'
dummy_object.age = 36

# Update of name attribute
dummy_object.name = 'dummy_name_test'

# Delete the name attribute
del dummy_object.name

# 2. NestedNamespace
class NestedNamespace(SimpleNamespace):
  def __init__(self, dictionary, **kwargs):
    super().__init__(**kwargs)
    for key, value in dictionary.items():
      if isinstance(value, dict):
        self.__setattr__(key, NestedNamespace(value))
      else:
        self.__setattr__(key, value)

d = {
  'parent': {
    'child': {
      'grandchild': 'value'
    }
  },
  'normal_key': 'normal value',
}
nested_namespace = NestedNamespace(d)

print(nested_namespace.parent.child.grandchild)  # value
print(nested_namespace.normal_key)  # normal value

# 2. Box
from box import Box

b = Box(d)
print(b.parent.child.grandchild)  # value
print(b.normal_key)  # normal value

# b.to_json(filpath)
filename = 'data/json_file.json'
b = Box.from_json(filename=filename)
print(b.name)
