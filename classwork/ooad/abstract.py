# from abc import ABC, abstractmethod

# # # class Person(ABC):
# # #   @abstractmethod
# # #   def sleep(self):
# # #     ...

# # #   def run(self):
# # #     print("Hello")



# # # class SuperPerson(Person):
# # #   @abstractmethod
# # #   def fly(self):
# # #     ...



# # # p = Person()


# # # class Student(Person):
# # #   def sleep(self):
# # #     print("Student sleeps")

# # #   def run(self, x):
# # #     pass


# # # s = Student()
# # # s.sleep()



# # class Vehicle(ABC):

# #   def __init__(self, model):
# #     self.__model = model
# #   @abstractmethod
# #   def get_max_speed(self):
# #     return "200km/h"
  
# # class Car(Vehicle):
# #   def get_max_speed(self):
# #     return super().get_max_speed()


# # class Motocylce(Vehicle):
# #   def get_max_speed(self):
# #     return super().get_max_speed()


# # class Airplane(Vehicle):
# #   def get_max_speed(self):
# #     return "400km/h"
  


# # car = Car("Audi")
# # moto = Motocylce("Suzuki")
# # # print(car.get_max_speed())
# # # print(moto.get_max_speed())

# # from typing import Sized, Container, Iterable, Sequence


# # class CustomList:
# #   def __len__(self):
# #     print("hello len")
# #     return 0
  
# # # c = CustomList()
# # # ls = []
# # # print(isinstance(c, Sized))
# # # print(isinstance(ls, Sized))

# # # print(list.mro())
# # # print(CustomList.mro())


# # class Person(ABC):
# #   @abstractmethod
# #   def sleep(self):
# #     ...



# # class Student:
# #   def sleep(self):
# #     print("hello")


# # Person.register(Student)

# # s = Student()

# # s.sleep()

# # print(isinstance(s, Person))
# # print(Student.mro())

# # class Chlp:
# #   pass

# # Person.register(Chlp)

# # ch = Chlp()

# # print(isinstance(ch, Person))

# # def method(p: Person):
# #   if isinstance(p, Person):
# #     p.sleep()


# # method(ch)

# from typing import Protocol, runtime_checkable

# # @runtime_checkable
# # class Person(Protocol):
# #   def foo(self):
# #     ...



# # class Mlass:
# #   def foo(self):
# #     print("hello world")


# # m = Mlass()

# # m.foo()

# # print(isinstance(m, Person))
# # print(Mlass.mro())

def custom_abstract(fn):
  fn.__isabstractmethod__ = True
  return fn

from abc import ABC
class Mlass(ABC):
  @custom_abstract
  def foo(self):
    ...
from typing import overload

@overload
def foo(a: int):
  pass

@overload
def foo(a: str):
  pass


def foo_any(a: any):
  foo(a)


foo_any(23)
# ob = Mlass()