# Version 1 before Encapsulation (Getters and Setters)

class Student:
  Number_Of_Students = 0

  def __init__(self, Name='Unknown', Age=0, Courses='none'):
    self.name = Name  #Instance Attribute
    self.age = Age
    self.courses = Courses
    Student.Number_Of_Students += 1

  def describe(self):  #Instace Method
    print(f"My name is {self.name} and I am {self.age} years old.")
    #print("My name is {} and I am {} years old.".format(self.name, self.age))

  def is_old(self, num):
    if self.age <= num:
      print("Student is not old")
    else:
      print("Student is old")


Student_1 = Student("Ahmed", 20, ["Math", "English"])
Student_2 = Student("Ali", 23, ["Math", "English"])

print(Student.Number_Of_Students)
print(Student_1.name, Student_1.age, Student_1.courses)
print(Student_2.name, Student_2.age, Student_2.courses)
print(Student_1 == Student_2)  # Check if the two objects are the same
print(id(Student_1), id(Student_2))  # print address of Obj
Student_1.describe()
Student_2.is_old(50)

__________________________________________________________________________________________

# Version 2 With Encapsulation (Getters and Setters) to Instance Attributes

class Student:
  Number_Of_Students = 0

  def __init__(self, Name='Unknown', Age=0, Courses='none'):
    self.__name = Name  #Instance Attribute
    self.__age = Age
    self.__courses = Courses
    Student.Number_Of_Students += 1

  def describe(self):  #Instace Method
    print(f"My name is {self.__name} and I am {self.__age} years old.")

  def get_name(self):
    return self.__name

  def set_name(self, new_name):
    self.__name = new_name

  def get_age(self):
    return self.__age

  def set_age(self, new_age):
    self.__age = new_age
    
Student_1 = Student("Ahmed", 20, ["Math", "OOP"])
Student_1.set_name('abdallah')
Student_1.set_age(24)
Student_1.describe()

________________________________________________________________________________________________

from datetime import date


class Student:

  def __init__(self, Name='Unknown', Age=0):
    self.name = Name  #Instance Attribute
    self.age = Age

  def describe(self):  #Instace Method
    print(f"My name is {self.name} and I am {self.age} years old.")

  @classmethod
  def initFromBirthYear(cls, Name, BirthYear):
    return cls(Name, date.today().year - BirthYear)

____________________________________________________________________________________________________

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

_____________________________________________________________________________________________________________
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

______________________________________________________________________________________________________ -___-




