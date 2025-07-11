
class Student(object):
  def __init__(self, score):
    self.__score = score
  
  @property
  def score(self):
    return self.__score
  
  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer')
    if value < 0 or value > 100:
      raise ValueError('score must be between 0 and 100')
    self.__score = value

s = Student(60)
print(s.score)  # Accessing the score property
s.score = 85  # Setting a new score
print(s.score)  # Accessing the updated score
s.score = 110  # This will raise a ValueError
s.score = 'A'  # This will also raise a ValueError
