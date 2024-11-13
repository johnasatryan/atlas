# # class Person:
# #   def __init__(self, name, age):
# #     self.__name = name 
# #     self.__age = age

# #   def __repr__(self):
# #     print("repr called...")
# #     return f"Person({self.__name}, {self.__age})"
  
# #   def __str__(self):
# #     return f"{{{self.__name }: {self.__age}}}"


# # p = Person("James", 13)

# # print(p)
# # print(repr(p))

# # +, -, *, /, //, **
# class Vector:
#   def __init__(self, *components):
#     self.components = components

#   @property
#   def components(self):
#     return self.__components
  
#   @components.setter
#   def components(self, values):
#     if not hasattr(values, '__iter__'):
#       raise TypeError
    
#     self.__components = values

#   def __str__(self):
#     return f"{self.components}"

#   def __add__(self, other):

#     if isinstance(other, tuple):
#       min_length = min(len(self.components), len(other))

#       components = (self.components[i] + other[i] for i in range(min_length))
#       return Vector(*components)
#     if not isinstance(other, Vector):
#       raise TypeError("Something went wrong in + operator...")
#     min_length = min(len(self.components), len(other.components))
#     components = (self.components[i] + other.components[i] for i in range(min_length))
#     return Vector(*components)

#   def __iadd__(self, other):
#     self = self + other
#     return self
  
#   def __radd__(self, other):
#     return Vector(*other) + self

  
#   def __floordiv__(self, other):
#     print("floor")

#   def __truediv__(self, other):
#     print("true")

#   def __pow__(self, value: float):
#     print("pow")
  

# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5)

# v3 = v1 + (5, 3)

# # print(v3)

# v4 = (5, 3) + v1


# print(v4)


class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __lt__(self, other):
    return self.x < other.x and self.y < other.y
  
  def __le__(self, other):
    return self < other or self == other


  # def __eq__(self, other):
  #   return  self.x == other.x and self.y == other.y
  
  # def __hash__(self):
  #   return hash(id(self))
  

  
  





v1 = Vector(5, 2)
v2 = Vector(5, 2)


# print(hash(v1))
# print(v1 < v2)
# print(v1 > v2)
# print(v1 == v2)
# print(v1 != v2)


class Person:
  def __bool__(self):
    print("bool called")
    return False
  def __len__(self):
    print("hello boolean")
    return 5



from functools import partial


class custom_partial:
  def __init__(self, fn, *args, **kwargs):
    self.__args = args
    self.__kwargs = kwargs
    self.__fn = fn

  def __call__(self, *args, **kwargs):
    pos_arguments = self.__args + args
    self.__kwargs.update(kwargs)
    return self.__fn(*pos_arguments, **self.__kwargs)


def add(a, b, c):
  print("hello world")
  return a + b +c

# add = custom_partial(add, 1, 2)

# print(add(4))

class decorator:
  def __init__(self, cls):
    self.__cls = cls

  def __call__(self, *args, **kwargs):
    print(f"Class name is: {self.__cls.__name__}")
    print("Class attributes: ")

    attributes = self.__cls.__dict__
    instance__attributes = []
    instance = self.__cls(*args, **kwargs)
    if instance is None:
      instance__attributes = []

    instance__attributes = instance.__dict__
   

    for attr in attributes:
      if attr.startswith('__'):
        continue
      print(f"- {attr}")
    print("Instance attributes: ")

    for attr in instance__attributes:
      print(f"- {attr}")
    




class Person:
  def __init__(self):
    self.name = ""
    self.age = 23
  def foo():
    pass

Person = decorator(Person)


# p = Person()



def decorator(fn):
  def wrapper(*args, **kwargs):
    pass
  pass

class decorator:
  def __init__(self, fn):
    self.__fn = fn

  def __call__(self, *args, **kwargs):
    pass


class custom_list:
  def __init__(self, *iterable):
    self.__arr = list(iterable)

  def __getitem__(self, index: int):
    print("subscript called...")
    return self.__arr[index]
  
  def __setitem__(self, index, value):
    raise AttributeError("Our list is not mutable")
  

# ls = custom_list(1, 2 ,3, 4)

# print(ls[3])

# ls[3] = 34


class Person:
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email
    self.i = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.i < len(self.__dict__):
      ls = list(self.__dict__)  
      res = self.__dict__[ls[self.i]]
      self.i += 1
      return res
    else:
      raise StopIteration
  


p = Person("James", 23, "email@example.com")

for item in p:
  print(item)
    

from typing import Container

class Mlass:
  def __contains__(self, value):
    print("hello in operator")
    print(value)
    return False
  
  def __len__(self):
    pass
  

m = Mlass()
5 in m