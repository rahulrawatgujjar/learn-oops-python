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

"""

class Grandfather:
  def wealth(self):
    print("Rich")

class Father(Grandfather):
  def height(self):
    print("Tall")


class Child(Father):
  def skills(self):
    print("Athlete")


child = Child()
child.skills()        # Athlete
child.height()        # Tall
child.wealth()        # Rich

