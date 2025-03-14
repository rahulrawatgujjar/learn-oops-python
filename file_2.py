#  Modify the Car class to encapsulate the brand attribute,
#   make it private, and provide a getter method for it


"""
Encapsulation:
  1. Bundling the data (attributes) and methods (functions) 
      that operate on the data into a single unit.
  2. Process of hiding internal state of object and requiring all interactions 
      to be performed through an object's method

It can be achieved using:

Public member:
  Can be accessed outside the class

Protected member:
  Can be accessed in class and subclass
  Can not be accessed outside the class (note that: python do not enforce strict access control)
  Use single underscore i.e. _ in the starting of variable name

Private member:
  Can only be accessed in the class in which it is defined
  Use double underscore i.e. __ in the starting of variable name( Note that: there is strict access control)
"""




class Car:

  def __init__(self,brand,model):
    self._brand=brand       # single undersoore means protected
    self.__model=model      # double underscore means private

  def fullName(self):
    return f"{self.brand} {self.model}"
  
  def get_brand(self):        # Defined a method to access protected data member by an object outside the class
    return self._brand
  
  def get_model(self):        # Defined a method to access private data member by an object outside the class
    return self.__model


class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size


if __name__=="__main__":

  myCar=ElectricCar("Tesla","Model S","100kWh")

  print(myCar.get_brand())  # Tesla
  print(myCar._brand)       # Tesla     ( It is accessible. _ is used as convention. It means no strict enforcement. So not recommended to access here)
  print(myCar.get_model())  # Model S
  print(myCar.__model)      # AttributeError: 'ElectricCar' object has no attribute '__model'. Did you mean: 'get_model'?






  
