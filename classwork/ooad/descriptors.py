# class Point2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   @property
#   def x(self):
#     return self.__x
  
#   @x.setter
#   def x(self, value):
#     if not isinstance(value, int):
#       raise ValueError
    
#     self.__x = value

#   @property
#   def y(self):
#     return self.__y
  
#   @y.setter
#   def y(self, value):
#     if not isinstance(value, int):
#       raise ValueError
    
#     self.__y = value


# p = Point2D(2, 54)

# # print(p.x)
# # print(p.y)

# class IntegerValue:
#   def __get__(self, instance, owner):
#     if instance is None:
#       return self
#     return self.__value

#   def __set__(self, instance, value):
#     if not isinstance(value, int):
#       raise ValueError
#     self.__value = value


# # class Point2D:
# #   x = IntegerValue()
# #   y = IntegerValue()


# # p = Point2D()
# # p.x = 23
# # p.y = 24
# # print(p.x)
# # print(p.y)

# # p2 = Point2D()
# # print(p2.x)
# # p2.x = 88
# # print(p.x)


# from random import choice, seed


# # class Game:
# #   def suit(self):
# #     return choice(('Heart', 'Club', 'Diamond', 'Spade'))
  
# #   def card(self):
# #     return choice(tuple('6789JQKA')+ ('10',))
  
# class Choice:
#   def __init__(self, *choices):
#     self.choices = choices

#   def __get__(self, instance, owner):
#     return choice(self.choices)


# class Game:
#   suit = Choice('Heart', 'Club', 'Diamond', 'Spade')
#   card = Choice(*'6789JQKA' + '10')

# durak = Game()

# for _ in range(6):
#   print(durak.suit, durak.card)


class IntegerValue:

  def __get__(self, instance, owner):
    if instance is None:
      return self
    return instance.some_value

  def __set__(self, instance, value):
    if not isinstance(value, int):
      raise ValueError
    instance.some_value = value


class Point2d:
  x = IntegerValue()
  y = IntegerValue()


p1 = Point2d()
p2 = Point2d()




class IntegerValue:
  def __init__(self, name):
    self.name = '__' + name

  def __get__(self, instance, owner):
    if instance is None:
      return self
    return getattr(instance, self.name)

  def __set__(self, instance, value):
    if not isinstance(value, int):
      raise ValueError
    setattr(instance, self.name, value)


class Point2d:
  x = IntegerValue('x')
  y = IntegerValue('y')










# class Counter:
#   def __init__(self, start):
#     self.start = start + 1

#   def __get__(self, instance, owner):
#     if instance is None:
#       return self
#     self.start -= 1
#     return self.start
  

# class Rocket:
#   counter = Counter(10)


# rocket1 = Rocket()
# rocket2 = Rocket()

# print(rocket1.counter)
# print(rocket2.counter)
# print(rocket2.counter)


import weakref
# class IntegerValue:
#   def __init__(self):
#     self.value = weakref.WeakKeyDictionary()

#   def __get__(self, instance, owner):
#     if instance is None:
#       return self
#     return self.value.get(instance)

#   def __set__(self, instance, value):
#     if not isinstance(value, int):
#       raise ValueError
#     self.value[instance] = value

  # def __delete__(self, instance):
  #   print('hello world')
  #   del self.value[instance]


# class Point2d:
#   x = IntegerValue()
#   y = IntegerValue()

#   def __repr__(self):
#     return str(id(self))
  




# p1 = Point2d()
# p2 = Point2d()


# p1.x = 24
# p2.x = 88

# print(p1.x)

# del p1
# del p2
# print(list(Point2d.x.__dict__['value'].items()))



class IntegerValue:

  def __set_name__(self, instance, name):
    self.name = '__' + name
 

  def __get__(self, instance, owner):
    if instance is None:
      return self
    return getattr(instance, self.name)

  def __set__(self, instance, value):
    if not isinstance(value, int):
      raise ValueError
    setattr(instance, self.name, value)


class Point:
  x = IntegerValue()




