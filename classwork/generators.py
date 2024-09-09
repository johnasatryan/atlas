# # def add(a:int, b: int)->int:
# #   return a + b


# # obj = map(add, [1, 2, 3, 4], [1, 2, 3, 4])
# # # print(obj)
# # # print(list(obj))


# # # iterables = ([1, 2, 3, 4], (1, 2, 3, 4), [1, 2, 3])

# # def custom_map(fn, *iterables):
# #   min_length = len(iterables[0])

# #   # for item in iterables[1:]:
# #   #   if min_length > len(item):
# #   #     min_length = len(item)

# #   for index in range(1, len(iterables)):
# #     if min_length > len(iterables[index]):
# #       min_length = len(iterables[index])

# #   min_length = min([len(item) for item in iterables])


# #   res = []


# # def foo():
# #   yield 1


# # x = foo()

# # print(x)
# # # print(next(x))
# # # print(next(x))
# # print(list(x))



# # def foo():
# #   for i in range(100000):
# #     yield i

# # item = foo()

# # for i in item:
# #   if i == 647:
# #     print("gtel em")
# #     break

# # print(next(item))



# def foo():
#   for i in range(5):
#     yield i + 1 # function will stop here
#     print("hello generator")

# item = foo()

# # print(next(item))
# # print(next(item))


# def foo(i):
#   if i > 0:
#     yield 1
#   else: 
#     print("hello world")

#     return 


# x = foo(-5)
# print(x)
# print(next(x))
# # print(next(x))

# # print(list(x))


def some():
  for i in range(5):
    yield i


gen = some()

# print(gen.gi_frame.f_locals)
item = gen


# print(next(gen))
# print(next(item))
# print(list(item))

import array

# item = (x for x in range(5))
# list_compr = [x for x in range(5)]

# {(x, y) for x in range(10)}

# x = array.array('i', [1, 2, 3, 4])

# print(x[0])



# def some_filter(x):
#   if x > 2:
#     return x ** 2

# itm = [some_filter(x) for x in range(1, 5)]

# print(itm)

def custom_map(fn, *iterables):
  min_length = len(iterables[0])

  # for item in iterables[1:]:
  #   if min_length > len(item):
  #     min_length = len(item)

  for index in range(1, len(iterables)):
    if min_length > len(iterables[index]):
      min_length = len(iterables[index])

  min_length = min((len(item) for item in iterables))

  res = []
  for index in range(min_length):
    temp = []
    for item in iterables:
      temp.append(item[index])
      # print(item)
      # print("---------->")
    res.append(fn(*temp))
    # print('<-------------')
  return res



print(custom_map(lambda x, y : x + y, [1, 2], [4, 5, 6]))

print(list(zip([1, 2, 3], [4, 5])))