# Abstraction:
#   Hiding internal implementation detials of a class and exposing only necessary 


"""
Abstract class:
  A class whose objects can not be created.
  It is meant to be inherited by other classes.

Abstract method:
  A method declared in Abstract class that do not have any implementation.
  It must be implemented in child class.

Note that:
  Use the ABC class from the abc module and the @abstractmethod decorator 
  to define abstract methods.

"""



# Defining an Abstract class

from abc import ABC, abstractmethod


class Shape(ABC):       # Abstract class

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass



# Implementing an Abstract class

class Circle(Shape):

  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return 3.14*(self.radius**2)
  
  def perimeter(self):
    return 2*3.14*self.radius
  



# shape = Shape()           # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

circle = Circle(3)
print(circle.area())          # 28.26
print(circle.perimeter())     # 18.84

