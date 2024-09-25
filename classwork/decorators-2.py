# # @decorator
# # def foo(n):
# #   if n == 0:
# #     return
# #   print("real function: ", n)
# #   foo(n - 1)


# # foo(5)

# # # def decorator(fn):
# #   def wrapper(*args, **kwargs):
# #     print("hello decorator")
# #     return fn(*args, **kwargs)
# #   return wrapper

# import sys

# def custom_wraps(origin_function: callable):
#   import inspect
#   def x(wrapper_function: callable):
#     wrapper_function.__doc__ = origin_function.__doc__
#     wrapper_function.__name__ = origin_function.__name__
#     wrapper_function.__signature__ = inspect.signature(origin_function)
#     return wrapper_function
#   return x
  
# def timed(fn):
#   from time import perf_counter
#   from functools import wraps

#   @custom_wraps(fn)
#   def wrapper(*args, **kwargs):
#     start = perf_counter()
#     result = fn(*args, **kwargs)
#     end = perf_counter()
#     elipsed = end - start

#     args_ = [str(x) for x in args]
#     kwargs_ = [f"{key}: {value}" for (key, value) in kwargs.items()]

#     all_args = args_ + kwargs_
#     all_args = ",".join(all_args)

#     print("{0}({1}) takes {2:.6f} seconds...".format(fn.__name__, all_args, elipsed))
#     return result
  
#   return wrapper

# def memoize(fn):
#   cache = {}
#   def wrapper(*args, **kwargs):
#     # keys = (args, tuple(kwargs.keys()))
#     if not args in cache:
#       cache[args] = fn(*args, **kwargs)
    
#     print(sys.getsizeof(cache))
#     return cache[args]
#   return wrapper


# def recursive_fib(n):
#   if n <= 2:
#     return 1
#   return recursive_fib(n - 1) + recursive_fib(n - 2)

# # recursive_fib(3)

# # @timed




# @timed
# @memoize
# def some_wrapper_for_fib(n):
#   return recursive_fib(n)


# some_wrapper_for_fib(30)
# some_wrapper_for_fib(20)


def getValue(ls: list, index: int)->int:
  return ls[index]

ls =[1, 2, 3]
index = 3

a ++
try:
  getValue(ls, index)
except BaseException as e:
  print(e)

print("hello world")