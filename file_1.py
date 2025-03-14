# Create a ElectricCar class that inherit from Car class and has an additional attribute battery_size

class Car:

  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  def fullName(self):
    return f"{self.brand} {self.model}"
  


class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size


if __name__=="__main__":
  myCar=ElectricCar("Tesla","Model S","100kWh")
  print(myCar.brand)            # Tesla
  print(myCar.battery_size)     # 100kWh
  print(myCar.fullName())       # Tesla Model S
  
