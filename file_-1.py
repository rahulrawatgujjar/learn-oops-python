# create a Car class with attributes like brand and model.
#   Then create instance of this class.

class Car:
  # constructor:
  #   It is used to initialize the objects.
  #   It is automatically called when an object is created.
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model



if __name__=="__main__":

  my_car=Car("Toyota","Fortuner")
  print(my_car.brand)
  print(my_car.model)

  my_car_2=Car("Tata","Safari")
  print(my_car_2.brand)
  print(my_car_2.model)