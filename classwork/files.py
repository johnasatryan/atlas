# # # Files 

# # # print(help(open))

# # # first argument file path, relative & absolute 
# # # second argument mode, context manager-> with
# # # fs = open('file.txt', mode='w')
# # # fs.write("hello world")

# # # with open('file.txt') as fs:
# # #   print(fs.read())

# # # print(help(open))

# # # fs = open('file.txt', mode='w+')
# # # print(fs.read())
# # # fs.write("bye")
# # # print(help(open))

# # # fs = open('file.txt', mode='w', encoding='utf-8', errors='backslashreplace')

# # # fs.write('հելլո վորլդ')

# # import os 



# # # fd = os.open('file.txt', os.O_RDONLY)
# # # print(fd)

# # # fs = open(fd, mode='w', closefd=False)
# # # fs = open('file.txt')

# # # fs.close()

# # # print(fs.fileno())



# # # def custom_opener(path, flags):
# # #   print(r'Before file opening')
# # #   return os.open(path, flags)


# # # fs = open('հո.txt', mode='w', opener=custom_opener)

# # # # fs.write("hello world")

# # # # print(help(open))
# # # import json

# # # fd = os.open('file.txt', os.O_RDONLY)


# # # fs = open('file.txt', mode='r')


# # # # print(fs.read())
# # # # # fs.seek(0)
# # # # print(fs.tell())
# # # # print(fs.read())

# # # print(help(fs))

# # class Found(Exception):
# #   pass

# # def getMatrix(matrix):
# #   for i in range(len(matrix)):
# #     for j in range(len(matrix[0])):
# #       if matrix[i][j] == 5:
# #         raise Found("Target found")
      

# # try:
# #   matrix = [[i + y for i in range(3)] for y in range(1, 10, 3)]
# #   print(matrix)
# #   getMatrix(matrix)

# # except Found as e:
# #   print(e)


# # def input(number: int)->None:

# #   assert number > 0, "Number cannot be less than 0"
#   # some code 


# # try:
# #   input(-5)

# # except ValueError as e:
# #   print(e)
# # except IndexError as e:
# #   print(e)

# # except AssertionError as e:
# #   print(e)


# # def validator(x : int):
# #   if x < 0 :
# #     raise IndexError("x must be greater than 0")
# #   return x + 1

# # while True:
# #   try:
# #     x = int(input("Enter x: "))
# #     validator(x)
# #     break
# #   except (ValueError, IndexError) as e:
# #     print(e)
# #     print("again")

# # print(x)

# # try/finally

# def fileHandler(path):
#   try:
#     fs = open(path, mode='w+', encoding='utf-8')
#     fs.write("հելլո")
#     # return fs.read()
#   except UnicodeEncodeError as e:
#     return e
#   except FileNotFoundError as e:
#     return 
#   else:
#     print("else called")
#   finally:
#     print("finally works anytime...")
#     try:
#       fs.close()
#     except UnboundLocalError:
#       print("normal krutit")
  





# print(fileHandler('file2.txt'))


# try:
#   5 / 1
# except ZeroDivisionError:
#   pass
# else:
#   print("else block")


def fileHandler(path):
  try:
    fs = open(path, mode='w+',encoding='ascii')
    fs.write('հելլօ')
    return fs.read()
  except UnicodeEncodeError as e:
    print("hello except")
    return e
  finally:
    # return 64
    print('finally')


while True:
  try:
    print(5)
  except KeyboardInterrupt:
    print("Minchev durs gale")
    break

  


print(fileHandler('file.txt'))