"""
Static method:
  It is a method that belong to a class rather than an object of the class.
  It do not have access to objects data.
  It is defined using @staticmethod decorator.
  It can access Class variables.
  
"""

class Car:

  car_count=0

  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
    Car.car_count+=1

  @staticmethod
  def get_count():
    return f"Count of car is {Car.car_count}"


class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size



if __name__=="__main__":

  myCar=ElectricCar("Tesla","Model S","100kWh")
  hisCar=Car("Tata","Safari")
  print(Car.get_count())          # Count of car is 2











  
