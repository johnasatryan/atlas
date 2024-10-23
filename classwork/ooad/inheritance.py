# # # # 

# # # class A:
# # #   pass

# # # # print(type(type))


# # # class delClass:
# # #   def __delattr__(self, attr):
# # #     print(attr)


# # # ob = delClass()

# # # # ob.x = 23

# # # # del ob.x


# # # # print(dir(delClass))
# # # # print(delClass.__dict__)
# # # # print(ob.__dict__)


# # # class A:
# # #   def __init__(self):
# # #     self.x = 0
# # #   def foo(self):
# # #     pass
# # #   def __eq__(self, other):
# # #     return self.x == other.x
# # #   def __format__(self, format_spec: str) -> str:
# # #     return self.__repr__()
  
# # #   def __ge__(self, other):
# # #     return self.x >= other.x
    

# # # ob = A()
# # # ob2 = A()

# # # # print(ob == ob2)
# # # print(dir(A))
# # # # print(ob.__dict__)

# # # print(ob >= ob2)
# # # # print(ob)
# # # # print("some object which name is: {} ".format(ob))

# # # # class Animal:
# # # #   def eat(self):
# # # #     print("Eating...")

# # # # class Lion(Animal):
# # # #   def walk(self):
# # # #     print("Walking...")


# # # # l = Lion()
# # # # l.eat()


# # from typing import Any


# # class Vector:
# #   def __init__(self, x, y):
# #     self.x = x
# #     self.y = y

# #   def __repr__(self):
# #     return f"Vector({self.x}, {self.y})"
  
# #   def __eq__(self, other):
# #     return (self.x == other.x and self.y == other.y)
# #   def __hash__(self):
# #     print("hash was called...")
# #     return hash(id(self))
  

# # # print(dir(Vector))



# # class Mlass:
# #   def __new__(cls):
# #     print("__new__ called...")
# #     instance = super().__new__(cls)
# #     return instance
# #   def __init__(self):
# #     print('__init__ called...')




# # # # ob = Mlass()
# # # instance = Mlass.__new__(Mlass)
# # # instance.__init__()


# # class MyMeta(type):
# #   def __new__(mcls, name, bases, kwargs):
# #     print("hello metaclass new...")
# #     return super().__new__(mcls, name, bases, kwargs)

# #   def __init__(mcls, *args, **kwargs):
# #     print("hello world")
# #     super().__init__(mcls)
# #   def __call__(mcls, *args, **kwargs):
# #     instance = mcls.__new__(mcls)
# #     instance.__init__(*args, **kwargs)



# # class Chlp(metaclass=MyMeta):
# #   def __new__(cls):
# #     return super().__new__(cls)
  
# #   def __init__(self):
# #     print("Chlp init called....")

# # p = Chlp()


# class Vector:
#   def __new__(cls, *args, **kwargs):
   
#     return super().__new__(cls)

#   def __init__(self, x):
#     self.x = 23


# # p = Vector(3)  

# class custom_none:
#   _instance = None
#   def __new__(cls):
#     if cls._instance is None:
#       cls._instance = super().__new__(cls)
#     return cls._instance
#   def __init__(self):
#     print('__init__ called')


# # p1 = custom_none()

# # class Base:
# #   def __init__(self) -> None:
# #     print('base __init__ called...')

# #   def __init_subclass__(cls) -> None:
# #     raise Exception

# # class Derived(Base):
# #   def __init__(self):
# #     print('derived __init__ called...')


# # base = Base() # base init called
import re

email_regex = r"^[a-zA-Z0-9.%+-]+\@[a-zA-Z.+-]+\.[a-zA-Z]{2,}$"
def stringValidator(s):
  return re.match(email_regex, s)



# class Person:
#   def __init__(self, email):
#     if stringValidator(email):
#       self.email = email
  
#   @property
#   def email(self):
#     return self.__email

#   @email.setter
#   def email(self, value):
#     print("hello setter")
#     if value == "":
#       raise ValueError
    
#     self.__email = value

# class Student(Person):
#   def __init__(self, name, avg_score):
#     self.name = name
#     self.avg_score = avg_score

  
#   @property
#   def avg_score(self):
#     return self.__avg_score
  
#   @avg_score.setter
#   def avg_score(self, value: float):
#     self.__avg_score = value


# # s = Student("", 98)

# # print(s.name)



class Person:
  def __init__(self, email):
    if stringValidator(email):
      self.email = email
  
  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, value):
    print("hello setter")
    if value == "":
      raise ValueError
    
    self.__email = value

  def __repr__(self):
    return f"Person email : {self.email}"
  
  def __reduce__(self):
    print("hello reduce")
    return 



import pickle


p = Person("example@gmail.com")
with open('file.pkl', 'wb') as fs:
  pickle.dump(p, fs)



with open('file.pkl', 'rb') as fs:
  load = pickle.load(fs)


print(load)