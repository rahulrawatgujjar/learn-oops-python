# Inheritance:
#   Allow a class to inherit methods and attributes from another class

"""
Type of Inheritance:
  1. Single:
    A child class inherits from one parent class.

"""

class Animal:            # parent class
  def speak(self):
    print("Animal speaks")


class Dog(Animal):       # child class
  def bark(self):
    print("Dog barks")


dog=Dog()
dog.speak()       # Animal speaks
dog.bark()        # Dog barks

