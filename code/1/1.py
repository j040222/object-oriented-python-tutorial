
class Class:
   """Documentation for Class"""
   
   #
   # A class variable:
   #
   
   static_value_ = 12
   
   def __init__(self):
      #
      # An instance variable:
      #
      self.value_ = 456
   
   def function(self):
      return self.value_

#
# To create an instance of a class:
#

obj = Class()

#
# To call a class function:
#

print(obj.function())

#
# Class variables can be accessed and modified without
# instances:
#

Class.static_value_ = 123
print(obj.static_value_)                  # 123, not 12

#
# __doc__ is a valid attribute. It returns the documentation
# string associated with the class:
#

print(obj.__doc__)
print(Class.__doc__)

#
# Data members (like obj.value_) are called 'data
# attributes' in python. Function instance attributes are
# called 'methods'.
#

#
# The expression obj.function() implicitly binds self, so it
# is equivalent to these expressions:
#

print( Class.function(obj) )

f = obj.function
print( f() )
del f

#
# Methods can be assigned after instantiation and can be
# defined outside of the class. However, 'self' is only
# implicitly bound for function class attributes:
#

def function1(self, x):
   return x

obj.function1 = function1

print( obj.function1(obj, 1) )            # 1

class Class2:
   f = function1                          # binds 'self'

c = Class2()
print( c.f(1) )                           # 1

#
# Classes can inherit other classes, override base class
# functions, and call base class functions using super():
#

class A:
   def f(self, x):
      return (x + 1)

class B(A):
   def f(self, x):                        # An override
      return x
   
   def g(self, x):
      return super().f(x)                 # or A.f(self)

b = B()
print( b.f(1) )                           # 1, not 2
print( b.g(1) )                           # 2, not 1

#
# Multiple inheritance is also allowed:
#

class A:
   def f(self):
      return 1

class B():
   def f(self):
      return 2

class C(A,B):
   pass

#
# If functions with the same name are defined in multiple
# base classes, the first base class in the class argument
# list is called:
#

c = C()
print( c.f() )                            #  1


#
# 'Super' calls the next class upward in the 'method
# resolution order', which is the order in which overridden
# methods are resolved in inheriting classes:
#

class A():
   def f(self):
      super().f()
      print("A.f")

class B():
   def f(self):
      print("B.f")

class C(A,B):
   def f(self):
      super().f()
      print("C.f")

c = C()
print(C.__mro__)              # The MRO is C -> A -> B
c.f()                         # Calls C.f -> A.f -> B.f


#
# All methods in python are effectively virtual. So base
# classes can call derived class methods:
#

class A():
   def f(self):
      self.g()                # Allowed when B inherits A

class B(A):
   def g(self):
      print("g")

b = B()
b.f()

#
# Use isinstance to check whether an object (eg. b) is an
# instance of a class (by inheritance or otherwise). Use
# issubclass to check whether a class is derived from
# another (including, possibly, itself):
#

print(isinstance(b, A))       # True
print(issubclass(B, A))       # True
print(issubclass(A, A))       # Also true

#
# If a class (A) appears more than once in the hierarchy of
# another (C) then it still only appears once in the MRO:
#

class A(object):
   pass

class B(A):
   pass

class C(A):
   pass

class D(B, C):
   pass

print(D.__mro__)              # Contains A only once

#
# By convention, attributes beginning with _ are considered
# private implementation details (and subject to change):
#

class A:
   _private = 123             # Not quite "private"

#
# Name mangling. Class attributes that begin with __ (and
# which have no more than 1 trailing underscore) are
# automatically replaced with the prefix _classname__.
#

class A:
   __attribute = 123
   
   def f(self):
      print(self.__attribute) # Allowed

# print(A.__attribute)        # A.__attribute not found
print(A._A__attribute)        # 123

a = A()
a.f()                         # Allowed - 123

#
# Python provides several special builtin attributes as
# follows:
#

class A(object):
   def f(self):
      pass

class B(A):
   def g(self):
      pass

b = B()

#
# A dictionary of b's (writeable) attributes:
#

print(b.__dict__)

#
# The name of the class of b:
#

print(b.__class__)

#
# A tuple of the base classes of B:
#

print(B.__bases__)

#
# The name of B:
#

print(B.__name__)

#
# The qualified name of B:
#

print(B.__qualname__)

#
# The method resolution order of B:
#

print(B.__mro__)

#
# The subclasses of B:
#

print(B.__subclasses__)

