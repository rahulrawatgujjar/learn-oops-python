
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

"""


class Car:

  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  
  def fuel_type(self):
    return "Petrol"


class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size

  def fuel_type(self):            # Here we use method overriding
    return "Electic current"

if __name__=="__main__":

  myCar=ElectricCar("Tesla","Model S","100kWh")
  print(myCar.fuel_type())        # Electic current

  hisCar=Car("Tata","Safari")
  print(hisCar.fuel_type())       # Petrol








  
