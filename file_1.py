# Learn about methods

class Car:

  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  # Method:
  """
  It is a function which is called for an object of class
  """
  def fullName(self):
    return f"{self.brand} {self.model}"
  



if __name__=="__main__":

  my_car=Car("Toyota","Fortuner")
  print(my_car.brand)         # Toyota
  print(my_car.model)         # Fortuner
  print(my_car.fullName())    # Toyota Fortuner
