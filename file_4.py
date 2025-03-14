
"""
Polymorphism:
  The word "polymorphism" means "many forms," and in programming, 
  it refers to the ability of a single function, method, or operator 
  to work in different ways depending on the context.
"""


"""
Types of Polymorphism:

1. Through method overriding:
    Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
    The method in the subclass has the same name, parameters, and return type as the method in the superclass.

2. Through operator overloading:
    Python allows you to define how operators (like +, -, *, etc.) 
    behave for custom classes using special methods (also called magic methods or dunder methods).

"""


class Point:

  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __add__(self,other):
    return Point(self.x + other.x, self.y + other.y)
  
  def __str__(self):
    return f"Point({self.x},{self.y})"
  



if __name__=="__main__":
  p1=Point(1,2)
  p2=Point(2,3)
  p3=p1+p2
  print(p3.x, p3.y)     # 3 5

  print(p3)             # Point(3,5)








  
