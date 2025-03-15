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

Abstract property:
  It can be defined by using @property decorator along with @abstractmethod

Concrete method:
 It is implemented in abstract class
"""



# Defining an Abstract class

from abc import ABC, abstractmethod


class Shape(ABC):       # Abstract class

  @abstractmethod
  def area(self):
    pass

  def shape_info(self):       # concrete method
    return "Here is the information"



# Implementing an Abstract class

class Circle(Shape):

  def __init__(self,radius,type):
    self.radius=radius
    self._shape_type=type

  def area(self):
    return 3.14*(self.radius**2)
  



circle= Circle(3,"circle")
print(circle.shape_info())      # Here is the information

