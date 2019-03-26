class Person:
    x = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1.x)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Inheritence
#Use the pass keyword when you do not want to add any other properties or methods to the class.
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def printname(self):
      print(self.firstname, self.lastname, self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()