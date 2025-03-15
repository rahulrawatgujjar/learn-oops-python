# "Create a readonly property for attribute model using property decorator"


"""
Property decorator:
  The @property decorator in Python is a built-in feature 
  that allows you to define methods that can be accessed 
  like attributes.
  
"""

class Car:

  car_count=0

  def __init__(self,brand,model):
    self.brand=brand
    self._model=model
    Car.car_count+=1

  @property
  def model(self):
    return self._model



class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size




if __name__=="__main__":

  myCar=ElectricCar("Tesla","Model S","100kWh")
  hisCar=Car("Tata","Safari")
  print(hisCar.model)
  hisCar.model="Nexon"        # AttributeError: can't set attribute 'model'














  
