"""
Class variable:
  It is shared across all objects.
  It is defined directly inside the class.
  It can be accessed using class name and object name.
  It can be modified using the class name.
  If you try to modify a class variable using an instance, 
    it will create a new instance variable with the same name, 
    shadowing the class variable.
"""

class Car:

  car_count=0

  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
    Car.car_count+=1



class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size



if __name__=="__main__":

  myCar=ElectricCar("Tesla","Model S","100kWh")
  print(Car.car_count)          # 1
  hisCar=Car("Tata","Safari")
  print(Car.car_count)          # 2











  
