# # # # class Person:
# # # #   pass

# # # # p = Person()

# # # # p.age = 23
# # # # print(p.__dict__)

# # # # ls = []

# # # # ls.x = 23

# # # class Person:
# # #   __slots__ = 'name', 'age'

# # #   def __init__(self, name, age):
# # #     self.name = name
# # #     self.age = age
# # #     # self.hobbies = []


# # # p = Person("James", 34)

# # # print(p.name)
# # # print(p.age)

# # # # print(p.__dict__)

# # # # p.x = 23


# # # class Person:
# # #   __slots__ = 'name', 'age'

# # #   def __init__(self, name, age):
# # #     self.name = name
# # #     self.age = age


# # # class Student(Person):
# # #   __slots__ = 'student_id'
# # #   def __init__(self, name, age, student_id):
# # #     super().__init__(name, age)
# # #     self.student_id = student_id





# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age


# # class Student(Person):
# #   __slots__ = 'student_id'
# #   def __init__(self, name, age, student_id):
# #     super().__init__(name, age)
# #     self.student_id = student_id


# # s = Student('James', 23, 5)

# # print(s.__dict__)
# # print(s.__slots__)


# class Person:
#   __slots__ = '__name', '__age'

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   @property
#   def name(self):
#     return self.__name
  
#   @name.setter
#   def name(self, value):
#     self.__name = value

#   @property
#   def age(self):
#     return self.__age
  
#   @age.setter
#   def age(self, value):
#     self.__age = value


# p = Person("James", 23)

# # print(p.name)
# # Person.x = 23
# # # print(p.__slots__)
# # print(Person.__dict__)

# class Student(Person):
#   __slots__ = '__student_id'

#   def __init__(self, name, age, student_id):
#     super().__init__(name, age)

#     self.student_id = student_id

#   @property
#   def student_id(self):
#     return self.__student_id
  
#   @student_id.setter
#   def student_id(self, value):
#     self.__student_id = value


# s = Student('James', 23, 234234)
# # s.p = 23

# list.x = 23