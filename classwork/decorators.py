# # # def counter(fn):
# # #   count = 0
# # #   def inner(arg1, arg2):
# # #     nonlocal count;
# # #     count += 1
# # #     print("Function {} was called {} times.".format(fn.__name__, count))
# # #     return fn(arg1, arg2)
# # #   return inner


# # # @counter
# # # def add(x: int, y: int)->int:
# # #   return x + y


# # # add = counter(add)

# # # print(add(1, 2))
# # # print(add(4, 5))


# # # def foo(origin):
# # #   print(id(origin))
# # #   origin()


# # # @foo

# # # def real():
# # #   print("real function")

# # # # @foo ===== real = foo(real)


# # # # real = foo(real)
# # # print(id(real))


# # def counter(fn):
# #   count = 0
# #   def inner(*args, **kwargs):
# #     nonlocal count;
# #     count += 1
# #     print("Function {} was called {} times.".format(fn.__name__, count))
# #     print(f"Positional rguments of function are: {args}")
# #     print(f"Keyword rguments of function are: {kwargs}")
# #     result = fn(*args, **kwargs)
# #     return result

# #   return inner


# # @counter
# # def add(x: int, y: int)->int:
# #   return x + y

# # add(1, 2)

# # print()

# # @counter
# # def mul(x: int, y: int, z: int)->int:
# #   return x * y * z

# # @counter
# # def sub(*, a: int, b: int)->int:
# #   return a - b


# # # mul(1, 2, 3)

# # sub(a=1, b=2)

# import inspect


# def counter(fn):
#   from functools import wraps

#   count = 0

#   @wraps(fn)
#   def inner(*args, **kwargs):
#     nonlocal count;
#     count += 1
#     print("Function {} was called {} times.".format(fn.__name__, count))
#     print(f"Positional rguments of function are: {args}")
#     print(f"Keyword rguments of function are: {kwargs}")
#     result = fn(*args, **kwargs)
#     return result

#   # inner.__name__ = fn.__name__
#   # inner.__doc__ = fn.__doc__
#   # # inner.__annotations__ = fn.__annotations__
#   # inner.__signature__ = inspect.signature(fn)
  
#   return inner


# @counter
# def add(x: int, y: int)->int:
#   '''
#     This function perform addition, gets two arguments...
#     If you any addition information about this call 1-2123-345
#   '''
#   return x + y



# # print(add.__annotations__)
# # print(add.__doc__)
# # print(add.__name__)
# # # print(help(add))
# # add = counter(add)


# # print()
# # print(add.__annotations__)
# # print(add.__doc__)
# # print(add.__name__)
# # print(help(add))
# # print(help(print))
# # print(add.__signature__)

# # print(add.__annotations__)
# # print(add.__doc__)

# print(help(add))


# # print(inspect.signature(add))

# def temp(count):
#   def decorator(fn):
#     def wrapper(*args, **kwargs):
#       result = 0
#       for i in range(count):
#         print(f"Function was called {i + 1} times")
#       # result = fn(*args, **kwargs)
#       return fn(*args, **kwargs)
#     return wrapper
#   return decorator


# def factorial(n: int)->int:
#   return 1 if n <= 0 else n * factorial(n - 1)

# factorial = temp(5)(factorial)(5)
# print(help(factorial))




def counter(fn):

  count = 0

  @wraps(fn)
  def inner(*args, **kwargs):
    nonlocal count;
    count += 1
    print("Function {} was called {} times.".format(fn.__name__, count))
    print(f"Positional rguments of function are: {args}")
    print(f"Keyword rguments of function are: {kwargs}")
    result = fn(*args, **kwargs)
    return result

  # inner.__name__ = fn.__name__
  # inner.__doc__ = fn.__doc__
  # # inner.__annotations__ = fn.__annotations__
  # inner.__signature__ = inspect.signature(fn)
  
  return inner


def temp(count):
  print("temp was called")
  def decorator(fn):
    print("decorator was called...")
    def wrapper(*args, **kwargs):
      result = 0
      for i in range(count):
        print(f"Function was called {i + 1} times")
      # result = fn(*args, **kwargs)
      return fn(*args, **kwargs)
    return wrapper
  return decorator


@temp(5)
def factorial(n):
  return n



