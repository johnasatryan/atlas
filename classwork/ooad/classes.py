class Person:
  pass


# ob = Person()
# # print(Person.mro())
# # print(dir(Person))
# print(ob)

# ls = [1, 2, 4]

# # print(list.mro())

# def foo():
#   pass

# print(isinstance(foo, object))


# class Vector:
#   def __init__(self, x, y):
#     self.setX(x)
#     self.__y = y

#   def setX(self, value):
#     if type(value) != int:
#       raise ValueError("Value must be interger type...")
#     self.__x = value

#   def getX(self):
#     return self.__x


# v = Vector(1.1, 2)

# print(v.__dict__)

# # # v.x = 3.14

# v.__x = 24
# print(v.__dict__)
# # v._Vector__x = "hello"
# print(v.__dict__)

# # v.setX(3.14)



# class Vector:
#   a = 12

# class Some:
#   count = 0
#   def __init__(self) -> None:
#     Some.count += 1
#   def foo(self):
#     pass
# # print(help(property))


# some1 = Some()
# some2 = Some()

# print(some2.count)
# print(some2.__dict__)
# print(Some.__dict__)


# class Vector:
#   def __init__(self, x, y):
#     self.setX(x)
#     self.setY(y)

#   def setX(self, value):
#     if type(value) != int:
#       raise ValueError("Value must be interger type...")
#     self.__x = value

#   def setY(self, value):
#     if type(value) != int:
#       raise ValueError("Value must be interger type...")
#     self.__y = value

#   def getX(self):
#     print("hello world")
#     return self.__x
  
#   def getY(self):
#     return self.__y
  
#   x = property(getX, setX)



# v = Vector(1, 2)

# print(v.x)
# print(v.__dict__)
# print(Vector.__dict__)

# v.x = 2.1




class Vector:
  def __init__(self, x):
    self.__x = x

  def getX(self):
    return self.__x
  
 

  x = property(getX)



# v = Vector(1)
# print(v.x)
# print(Vector.x)

# Vector.x = 21




class custom_property:
  def __init__(self, fget = None, fset = None, fdel = None, doc = None):
    self.__fget = fget
    self.__fset = fset
    self.__fdel = fdel
    self.__doc = doc

  def __get__(self, chujoy_self, classi_ter):
    if chujoy_self is None:
      return self
    print(f"Custom property self: {self}")
    print(f"Te vor classi objectna sa: {chujoy_self}")
    print(f"Te vor classi hamar e stexcvel: {classi_ter}")
    return self.__fget(chujoy_self)
  
  def __set__(self, instance, value):
    if self.__fset is None:
      raise AttributeError(f"can't set attribute x")
    return self.__fset(instance, value)
  
  def setter(self, fn):
    print(f"setter function in class: {fn}")
    self.__fset = fn
    return self



class Vector:
  def __init__(self, x):
   self.x = x

  @custom_property
  def x(self):
    return self.__x

  @x.setter
  def x(self, value):
    print("sa kancvhuma")
    if type(value) != int:
      raise ValueError("inch vor ban...")
    self.__x = value
  x = property(None, x)


# print(Vector.__dict__)

v = Vector(1)

print(Vector.__dict__)
# print(v.x)

 
# v.x = 12


















