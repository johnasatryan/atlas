# # # class Employee:
# # #   def __init__(self, name):
# # #     self.name = name
# # #     print(f"{self.name} is an employee.")
  
# # #   def work(self):
# # #     print(f"{self.name} is working hard")


# # # class Manager(Employee):
# # #   def __init__(self, name, team_members):
# # #     self.name = name
# # #     self.team_members = team_members
  
# # #   def manage(self):
# # #     print(f"{self.name} manages team where {self.team_members}")


# # # class TechLead(Employee):
# # #   def __init__(self, name, tech_skills):
# # #     self.name = name
# # #     self.tech_skills = tech_skills
  
# # #   def experience(self):
# # #     print(f"{self.name} has set of skills: {self.tech_skills}")


# # # class SeniorManager(Manager, TechLead):
# # #   def __init__(self, name, team_members, tech_skills):
# # #     super().__init__(name, team_members)
# # #     # super(Manager, self).__init__(name, tech_skills)
# # #     TechLead.__init__(self, name, tech_skills)

# # #   def routine(self):
# # #     self.manage()
# # #     self.experience()


# # # senior = SeniorManager("Lucy", 13, "Python, OOAD, Software Design")
# # # # print(SeniorManager.mro())

# # # senior.routine()



# # class Shape:
# #   pass


# # class Circle(Shape):
# #   def __init__(self, r):
# #     print("Circle init")
# #     self.__r = r



# # class Square(Shape):
# #   def __init__(self, x):
# #     print("Square init")

# #     self.__x = x

# #   def perimeter(self):
# #     pass


# # class SquareCircle(Circle, Square):
# #   def __init__(self, x):
# #     super().__init__(x)



# # ob = SquareCircle(5)

# # print(SquareCircle.mro())


# class A:
#   pass
# class B: pass

# class C(A, B): pass

# class D(A, B): pass

# class E(D, C):pass

# print(f"Object's mro: {object.mro()}")
# print(f"A's mro: {A.mro()}")
# print(f"B's mro: {B.mro()}")
# print(f"C's mro: {C.mro()}")
# print(f"D's mro: {D.mro()}")
# print(f"E's mro: {E.mro()}")


# class I(C, A):
#   pass



# # class E(C, D): pass

# ob = I()

# print(ob)
# print(dir(ob))


# print(dir(type))


class mystring(str):
  def __setitem__(self, index, value):
    print(index)
    print(value)

# st = str("hello")
# st[0] = "a"
m = mystring("hello")
m[0] = "a"
print(m)
