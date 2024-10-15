class User():
  def __init__(self, name, birthyear):
      self.name = name
      self.birthyear = birthyear
  def get_name(self):
      return self.name.upper()
  def age(self, current_year):
      age = current_year - self.birthyear
      return age
john = User(name = 'John', birthyear = 1999)
print(john.age(current_year=2023))
print(john.get_name())