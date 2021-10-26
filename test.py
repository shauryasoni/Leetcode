class C(object):
       def __init__(self):
              self.c = 21
  
              # d is private instance variable 
              self.__d = 42 
              print(self.__d)   
class D(C):
       def __init__(self):
              self.e = 84
              C.__init__(self)


object1 = C()
  
# produces an error as d is private instance variable
print(object1.c) 