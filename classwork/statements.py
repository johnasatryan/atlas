# # # # # # if, else elif, assignments 

# # # # # # 1. 

# # # # # x = 213
# # # # # # if (x > 0):
# # # # # y = 1
# # # # # if (x > 0):
# # # # #   print()
# # # # #   x = 23
# # # # #   if y > 0:
# # # # #     pass


# # # # # spam = "spam"

# # # # # if spam = 12:
# # # # #   print(spam)


# # # # # const char* spam = "spam";

# # # # # if(spam = "s")
# # # # # {

# # # # # }

# # # # # warlus
# # # # # if x := 3:
# # # # #   pass


# # # # # if 5 == 5:

# # # # # if else else if == if else elif

# # # # ls = []

# # # # a = None
# # # # # &&, ||  == and, or 

# # # # if not ls:
# # # #   print("List is not empty")


# # # # if ls == False:
# # # #   pass


# # # # print(set() == False)
# # # # print(type(ls) == type(False))

# # # # if ls:
# # # #   pass

# # # # # pass is placeholder

# # # # # switch/case == match 

# # # # # operator = input("enter a symbol: ")

# # # # # if operator == '+':
# # # # #   # do addition
# # # # #   pass
# # # # # elif operator == '-':
# # # # #   pass

# # # # # match operator:
# # # # #   case '+':
# # # # #     # do addition
# # # # #     pass
# # # # #   case '-':
# # # # #     pass


# # # # # x = input("Enter a number: ")

# # # # # print(type(int(x)))

# # # # # Loops

# # # # # Iterables -> list, tuple, dict, set, string, file, range 
# # # # # __iter__ -> double underscore -> dunder

# # # # # print(dir(ls))
# # # # print(help(ls.__iter__))

# # # # iterator vv. iterable 
# # # # ls.__iter__() # implementation interpreter specific
# # # # iterator = iter(ls) # user friendly 

# # # # print(help(iterator))
# # # ls = [65, 44, 33, 40, 50, 10]


# # # iterator = iter(ls)
# # # # print(next(iterator))
# # # # print(next(iterator))
# # # # print(next(iterator))
# # # # stop = StopIteration()

# # # # try:
# # # #   next(iterator)
# # # # except StopIteration:
# # # #   print("Hasela stopi")

# # # # def forr(iterator):
# # # #   try:
# # # #     print(next(iterator))
# # # #     print(next(iterator))
# # # #     print(next(iterator))
# # # #   except StopIteration:
# # # #     return

# # # # forr(iterator)

# # # # for i in ls:
# # # #   print(i)

# # # # for(int i = 0; i < 5; ++i)

# # # # for i in range(len(ls)):
# # # #   print("index: ", i)
# # # #   print("value: ", ls[i])

# # # # print(len(ls))
# # # # print(range(len(ls)))

# # # # x = range(5)
# # # # print(list(x))
# # # # range(1, 4)
# # # # range(1, 10, 2)


# # # # enumerate 

# # # # print(help(enumerate))

# # # # print(list(enumerate(ls)))

# # # # st = {98, "hello", "a"}
# # # # st2 = {1, 2, 3, 4}
# # # # print(st)
# # # # # print(st2)
# # # # print(hash(98))
# # # # print(hash("hello"))


# # # def custom_enumerate(iterable, start=0):
# # #   res = []

# # #   # for index in range(len(iterable)):
# # #   #   res.append(tuple(start, iterable[index]))
# # #   #   start += 1

# # #   for item in iterable:
# # #     res.append((start, item))
# # #     start += 1

# # #   return res

# # # # print(custom_enumerate(ls, -354))
# # # # print(list(enumerate(ls, -354)))


# # # # print(range(5, 7))

# # # # for i in range(-10, -1, 1):
# # # #   print(i)

# # # print(ls)
# # # # print(ls[1])
# # # # [start: end: step]

# # # print(ls[1:3:2])
# # # print(ls[1:5:2])
# # # # print(ls[-1:])

# # # # ls2 = ls[-1:]

# # # # print(ls2)
# # # # print(len(ls2))
# # # ls2 = ls[:]

# # # ls3 = ls

# # # print(f"ls2 address: {id(ls2)}")
# # # print(f"ls address: {id(ls)}")
# # # print(f"ls3 address: {id(ls3)}")


# # ls = [1, 2, 3, 4, 54, 6]

# # # print(ls[2::-2])
# # # print(ls[5:1:-1])
# # # print(ls[::-1])

# # # print(ls[:2:-1])


# # def slicing(iterable, start = None, end=None, step = 1):
# #   res = []

# #   # print(ls[:4:-2])
# #   # if start > 0 and end < 0:
# #   #   end = len(iterable) + end

# #   # if start < 0 and end > 0:
# #   #   pass
# #   if step > 0 and end == None:
# #     end = len(iterable)
# #   if step < 0 and start == None:
# #     start = len(iterable) - 1
  
  
# #   if step < 0 and end == None:
# #     end = -1

 
# #     # tmp = start
# #     # start = end - 1
# #     # end = tmp - 1

# #   for i in range(start, end, step):
# #     res.append(iterable[i])
# #   return res

# # print(ls[::-1])
# # print(slicing(ls, None, None, -1))



# # print(ls)
# # print(ls[:4:-2])
# # print(slicing(ls, None, 4, -2))

# # print(ls[2::-2])
# # print(slicing(ls, 2, None, -2))


# # print(ls[1:-1])
# # print(slicing(ls, 1, -1))

# # # print(ls[-1:1])





# #  for / else or while/else 


# # for i in range(5):
# #   if i == 8:
# #     break
# # else:
# #   print("what is this???")


# ls = [x for x in range(5, 12, 2)]

# target = 7

# flag = False

# for i in ls:
#   if i == target:
#     flag = True


# # if flag:
# #   print("Founded")
# # else:
# #   print("not founded")


# for i in ls:
#   if i == target:
#     print("founded")
#     break
#   else:
#     pass
# else:
#   print("not founded")

# while True:
#   pass
# else:
#   pass


# int a = 10;

# if a > 0 ? true : False

a = 10 


# flag = True if a > 10 else False if a < 6 else 66

# print(flag)

def foo():
  print("hello")

# a and foo()

a = 1
b = 4
c = 3

# print(1 and c) a == b < c

# print(1 and 3)

# print(a == b and b < c)
# # print(a == b < c)

# print(0 or 6)


# if 0 or 5:
#   pass

# "hello" if a > 3 else False
# a > 3 and "hello" 