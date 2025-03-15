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

"""


class Animal:
  def speak(self):
    print("Animal speaks")

class Dog(Animal):
  def bark(self):
    print("Dog barks")

class Cat(Animal):
  def meow(self):
    print("Cat meows")



dog=Dog()
dog.bark()      # Dog barks
dog.speak()     # Animal speaks

cat=Cat()
cat.meow()      # Dog barks
cat.speak()     # Animal speaks
