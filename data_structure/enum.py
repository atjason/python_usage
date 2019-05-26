import enum

@enum.unique
class Color(enum.Enum):
  RED = 1
  GREEN = 2
  BLUE = enum.auto()

color = Color.RED
color == Color.RED