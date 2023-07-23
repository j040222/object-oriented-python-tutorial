#
# Lambda functions can accept any number of arguments
# and can be named. Lambdas can also be passed as arguments
# to other functions.
#

#
# Lambda functions should consist of one statement only.
# Multiple statements are not allowed. Lambda functions
# cannot contain statements, and including statements like
# return, assert and raise will cause a SyntaxError
# exception. There is no equivalent for type hinting with
# lambda functions. You cannot decorate a lambda function
# using the @decorator syntax.
#

f = lambda x : x                          #  Identity

print(f(1))                               #  1

f = lambda a, b, c : (a + b + c)

print(f(1,2,3))                           #  6

def f(g):
   return g

f(lambda x : print(x)) (1)                #  1

#
# Assign a custom docstring to a lambda function:
#

f.__doc__ = "A documentation string"
print(f.__doc__)

#
# There is very little difference between a function and
# a lambda function. Note, however, that lambda functions
# are not named in tracebacks:
#

f = lambda x : x / 0
# f(1)                                    #  Error: 1/0

print(f.__name__)                         #  <lambda>

#
# Lambda function arguments can be named (Ie. they can be
# keyword arguments) and varargs is allowed:
#

f = lambda a,b : (a + b)
print(f(b=1, a=2))                        #  3
print(f( *[1,2] ))                        #  3
print(f( **{ 'a':1, 'b':2 } ))            #  3

f = lambda **kwargs : sum(kwargs.values())
print(f(first=1, second=2))               #  3

#
# Like regular functions, a lambda function can also be a
# closure:
#

def f(x):
   y = 1
   return lambda z : (x + y + z)

g = f(1)
print(g(1))                               #  3

#
# In Python, lambda closure functions bind their arguments
# at execution time, not a definition time. This means that
# using a lambda as a closure in a loop can have unexpected
# effects:
#

functions = []
for i in range(3):
   functions.append(lambda : print(i))
for f in functions:
   f()                                    #  2 2 2, not 0 1 2

#
# Define the argument with a default value to overcome this:
#

functions = []
for i in range(3):
   functions.append(lambda x=i : print(x))
for f in functions:
   f()                                    #  0 1 2

#
# Class functions and class properties can be assigned using
# lambda functions. However, this practice is discouraged:
#

class A:
   def __init__(self, number):
      self._number = number
   number =                                                \
      property(
         lambda self : self._number,
         lambda self, value : setattr(self, '_number', value)
         )
   __str__ = lambda self : str(self.number)

a = A(1)
a.number = 2
print(a.number)                           #  2

