# Inheritance:
#   Allow a class to inherit methods and attributes from another class

"""
Type of Inheritance:
  1. Single:
    A child class inherits from one parent class.

  2. Mulitple:
    A child class inherits from multiple parent class.


"""

class Father:
  def height(self):
    print("Tall")

class Mother:
  def intelligence(self):
    print("Smart")

class Child(Father,Mother):
  def skills(self):
    print("Athlete")


child = Child()
child.skills()        # Athlete
child.height()        # Tall
child.intelligence()  # Smart

