import enum

@enum.unique
class Color(enum.Enum):
  RED = 1
  GREEN = 2
  BLUE = enum.auto()

color = Color.RED
color == Color.RED

class Types(str, enum.Enum):
  type1 = "Type1"
  type2 = "Type2"

print(Types.type1.value)
print(Types['type2'].value)

for type in Types:
  print(type.name, type.value)
