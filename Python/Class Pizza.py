class Pizza:

  def __init__(self, ingrediants):
    self.ingrediants = ingrediants

  @classmethod
  def veg(cls):
    return cls(['mushroom', 'onion', 'tomato'])

  @classmethod
  def marg(cls):
    return cls(['cheese', 'tomato', 'mushroom'])
  def __str__(self):
    return f"Pizza ingrediants are {self.ingrediants}"


pizza1 = Pizza(['tomato', 'mushroom'])
pizza2 = Pizza.veg()
pizza3 = Pizza.marg()
print(pizza1)
print(pizza2)
print(pizza3)

______________________________________________________________________________________________ -___-

class Math:

  @staticmethod
  def add(x, y):
    return x + y

  @staticmethod
  def add5(x):
    return x + 5

  @staticmethod
  def add10(x):
    return x + 10

  @staticmethod
  def PI():
    return 3.14


class Pizza:

  def __init__(self, radius, ingrediants):
    self.ingrediants = ingrediants
    self.raduis = radius

  def __str__(self):
    return f"Pizza ingrediants are {self.ingrediants}"

  def area(self):
    return Pizza.circle_area(self.raduis)

  @staticmethod
  def circle_area(r):
    return r**2 * Math.PI()


Pizza1 = Pizza(6, ["cheese", "tomato"])
print(Pizza1.area())
print(Pizza.circle_area(4))


