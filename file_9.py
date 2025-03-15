# Demonstrate the use of isinstance to check

class Car:

  car_count=0

  def __init__(self,brand,model):
    self.brand=brand
    self._model=model
    Car.car_count+=1




class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size




if __name__=="__main__":

  myCar=ElectricCar("Tesla","Model S","100kWh")

  print(isinstance(myCar,ElectricCar))      # True
  print(isinstance(myCar,Car))              # True














  
