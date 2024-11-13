
class MyMeta(type):
  def __new__(mcls, name, bases, kwargs):
    print('hello __new__')
    cls_instance = super().__new__(mcls, name, bases, kwargs)
    return cls_instance
  
  def __init__(cls, name, bases, kwargs):
    print('hello __init__')

  def __call__(self):
    print('hello __call__')

class Any:
  pass

# class Person(metaclass=MyMeta):
#   pass



# ob = Person()


class A:
  def __new__(cls, *args, **kwargs):
    print('__new__')
    return super().__new__(cls)

  def __init__(self):
    print('__init__')


ob = A()