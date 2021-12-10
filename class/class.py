
class Person:

  name = ''
  __age = 0 # private variable, starts with __; private method is similar.

  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def speak(self):
    print(f'I am {self.name}, {self.__age} years old.')

class Student(Person):

  grade = 0

  def __init__(self, name, age, grade):
    super().__init__(name, age) # call super init first.
    self.grade = grade
  
  def speak(self):
    super().speak()
    print(f'\tI am grade {self.grade}.')
  
s = Student('Tom', 10, 4)
s.speak()
