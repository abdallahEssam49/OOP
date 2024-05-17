class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    return f'Name : {self.name}, Age : {self.age}'

class Man(Person):
  Gender = 'Male'
  Number_Of_Men = 0

  def __init__(self, name, age, tall):
    super().__init__(name, age)
    self.tall = tall
    Man.Number_Of_Men += 1

  def display(self):
    string = super().display()
    return string + f'\tTall : {self.tall} , Gender : {self.Gender}'


class Woman(Person):
  Gender = 'Female'
  Number_Of_Women = 0

  def __init__(self, name, age, hair):
    super().__init__(name, age)
    self.hair = hair
    Woman.Number_Of_Women += 1

  def display(self):
    string = super().display()
    return string + f'\tHair : {self.hair} , Gender : {self.Gender}'


man1 = Man('Abdallah', 24, 176)
man2 = Man('Yousef', 15, 170)
print(man1.display())
print(man2.display())
print(Man.Number_Of_Men)

woman1 = Woman('nada', 20, 'Black')
print(woman1.display())
print(Woman.Number_Of_Women)
