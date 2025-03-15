"""
Constructor:

1. Default Constructor:
    If you don't define a constructor, Python provides 
    a default constructor that does nothing.

2. Parameterized Constructor:
    A constructor that accepts parameters to initialize attributes dynamically.

3. Constructor with default values:
    You can provide default values for constructor parameters.

4. Constructor overloading:
    Python does not support constructor overloading 
    (multiple constructors with different parameters) directly. 
    However, you can achieve similar functionality using default arguments or class methods.

"""



# Default constructor

class Person:
  pass

person = Person()       # Default constructor is called







# Parameterized constructor

class Rectangle:
  def __init__(self,l,b):                         # parameterized constructor
    self.length=l
    self.breadth=b

  def __str__(self):                              # only to print
    return f"L:{self.length} B:{self.breadth}"
  

a= Rectangle(2,3)
print(a)          # L:2 B:3







# Constructor with default values

class Circle:
  def __init__(self, r=1):    # default value of r is 1
    self.radius=r

c= Circle()
print(c.radius)     # Output : 1








# Constructor overloading

class Person:

  def __init__(self,name,age):
    self.name=name
    self.age=age

  @classmethod
  def from_DOB(cls,name,birth_year):       # alternate constructor
    return cls(name,2025-birth_year)
  
  def __str__(self):
    return f"{self.name} {self.age}"
  


p1=Person("rahul",24)
print(p1)                               # rahul 24

p2=Person.from_DOB("surender",2001)
print(p2)                               # surender 24

  











# 