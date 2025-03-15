# "Create a readonly property for attribute model using property decorator"


"""
Property decorator:
  The @property decorator in Python is a built-in feature 
  that allows you to define methods that can be accessed 
  like attributes.

  Getter decorator:
    @property decorator is generally used to define a getter.

  Setter decorator:
    It can optionally be used to define setter and deleter using the 
    @<property_name>.setter and @<property_name>.deleter decorators
  
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
  
  @model.setter             # Here is the setter decorator
  def model(self,value):
    if len(value)<3:
      raise ValueError("Model name must be at least 3 characters long")
    self._model=value



class ElectricCar(Car):

  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size




if __name__=="__main__":

  hisCar=Car("Tata","Safari")
  print(hisCar.model)       # Safari

  hisCar.model="Nexon"
  print(hisCar.model)       # Nexon     (now we are not getting attribute error)

  hisCar.model="ev"         # ValueError: Model name must be at least 3 characters long














  
