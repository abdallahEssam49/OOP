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
