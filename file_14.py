# Inheritance:
#   Allow a class to inherit methods and attributes from another class

"""
Type of Inheritance:
  1. Single:
    A child class inherits from one parent class.

  2. Multiple:
    A child class inherits from multiple parent class.

  3. Multilevel:
    A child inherits from parent class which in turn inherits from another class.

  4. Hierarchical:
    Mulitple child classes inherit from a single parent class.

  5. Hybrid:
    It is combination of 2 or more types of inheritance.

"""



class A:
  def method_a(self):
    print("Method A")

class B(A):
  def method_b(self):
    print("Method B")

class C(A):
  def method_c(self):
    print("Method C")

class D(B,C):
  def method_d(self):
    print("Method D")

#  B and C inherit from A, so hierarchical.
#  D inherit from B and C, so multiple.
#  D inherit from B and C, which in turn inherit from A, so multilevel.


d = D()
d.method_a()    # Method A
d.method_b()    # Method B
d.method_c()    # Method C
d.method_d()    # Method D



