"""
Class method:
  1. It operate on class variables instead of object's data.
  2. It can be called using class.
  3. It takes cls as first parameter to access or modify class variables.
  4. It is defined using @classmethod decorator.

  
Summary:

  Class Method:
    No access to object data (ie. no self parameter)
    Access to class attributes (ie. using cls parameter)

  Static Method:
    No access to object data (ie. no self parameter)
    No access to class attributes   (ie. no cls parameter)
    But has indirect access to class attributes (ie. using ClassName.ClassAttribueName)

"""



class Counter:
  count=0               # class attribute

  @classmethod
  def increment(cls):   # class method
    cls.count+=1

  @classmethod
  def get_count(cls):   # class method
    return cls.count
  



# calling class method using classname

Counter.increment()
print(Counter.get_count())    # 1










"""
Following information is extra. So skip it if do not want to be confused
"""

# Note that class methods can be called using object

c1= Counter()
c1.increment()
print(c1.get_count())   # 2

c2= Counter()
print(c2.get_count())   # 2
