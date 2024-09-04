# # # LEGB 
# # # closures 

# # # Local, Enclosing, Global, Built-in


# # # n = 5
# # # print(n)


# # # print = 23

# # # print(23)


# # # x = "hello"

# # # def foo():
# # #   global x;
# # #   x = 23


# # # foo()
# # # print(x)


# # # SIZE = 64
# # # class Deque:
# # #   def __init__(self, BLOCK_SIZE=SIZE):
# # #     self.BLOCK_SIZE = BLOCK_SIZE

# # # def foo(name = x):
# # #   print(name)


# # # x = "bye"

# # # foo()

# # # Enclosing 

# # # x = 23
# # # # nonlocal

# # # def base():

# # #   def pow(y):
# # #     global x;
# # #     x = 65
# # #     return x ** 2
# # #   return pow(5)


# # # var = base()



# # # x = 10

# # # def foo():
# # #   y = "hello"
# # #   def bar():
# # #     nonlocal y;
# # #     y = 44
# # #   bar()
# # #   return y


# # # print(foo())



# # # def f1():
# # #   x = 23

# # #   def f2():
# # #     # nonlocal x; 
# # #     x = -1
# # #     def f3():
# # #       nonlocal x
# # #       x = "hello"
# # #     f3()
# # #   f2()
# # #   print(x)

# # # f1()

# # # def factorial(n):
# # #   if n <= 1:
# # #     return 1
# # #   return n * 24



# # # factorial(4)
# # # if 4 <= 1
# #   # chi mtnum
# # # 4 * 6

# # # factorial(3)
# # # if 3 <= 1
# # # 3 * 2

# # # factorial(2)
# # # 2 * 1

# # # factorial(1)
# # # if i paymane bavararec, veradardz 1

# # # factorial(5)

# # # Functional Programming 


# # def foo(x):
# #   return x % 2 == 0


# # # iter = filter(foo, [1, 2, 3, 4, 5])

# # # for i in iter:
# # #   print(i)


# # # Higher order functions vs First class object(citizens)

# # # First class objects
# # # 1. when you can pass as function argument
# # # 2. return from functions
# # # 3. class or some other type, can be used as a container


# # # Higher order functions

# # # 1. when you can pass as function argument 
# # # 2. return from functions
# # # 3. must be callable

# # def foo(x):
# #   return "hello"


# # def custom_filter(fn, iterable):
# #   res = []

# #   for item in iterable:
# #     if fn(item):
# #       res.append(item)

# #   return res


# # iter = custom_filter(foo, [1, 2, 3, 4, 5])
# # iter = filter(foo, [1, 2, 3, 4, 5])
# # print(list(iter))

# # print(dir(int))


# # def base():
# #   x = 10

# #   def pow():
# #     nonlocal x
# #     x -= 1

# #   def pow2():
# #     nonlocal x
# #     x += 1

    
# #   return pow, pow2

# # tp = base()
# # # print(foo(5))

# # print(tp[0].__closure__)
# # print(tp[1].__closure__)

# # tp[0]()
# # tp[1]()

# # print(tp[0].__closure__)
# # print(tp[1].__closure__)


# x = "hello"


# # def base(x):
# #   def pow(n):
# #     return n ** x
# #   return pow

# # foo = base(5)

# # foo(3)

# # def foo():
# #   x = 23
# #   def bar():
# #     x = "hello"


# # lambda ananun 
# # 1. lambda 
# # 2. arguments list, no need parenteses, 
# # 3. by default body is returnabale entity 
# # 4. can assign to any name
# # filter(lambda )


# # a = lambda : lambda : 5

# # print(a()())


# # foo()()()()()()()()

# # foo = lambda : lambda : lambda : 3

# # print(foo()()())


# # ls = list(filter(lambda x : x % 2 == 0, [1, 2, 3, 4, 5]))

# # print(ls)


# # def foo()->int:
# #   print(2)

# # def foo(x: int):
# #   return x * 2

# # print(foo(3))


# def foo(n):
#   res = []

#   for i in range(1, n):
#     res.append(lambda x: i * n)
#   return res



# # i = 0
# # for fn in res:
# #   print(fn(i))
# #   i += 1



# res = foo(4)


# print(hex(id(3)))
# # for i in res:
# #   print(i.__closure__)
# #   print(i(3))


# # for i in range(4):
# #   pass

# # del i
# # print(i)

def foo():
  x = 23
  print(hex(id(x)))
  def bar1():
    def bar2():
      # print(x)
      pass
    return bar2
  print(bar1.__closure__)
  return bar1()

x = foo()
# print(x.__closure__)

# def foo():
#   x = 12
#   def bar():
#     x = 23
#   print(bar.__closure__)
#   bar()

# foo()