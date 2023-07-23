
#
# Nested functions can access variables in the enclosing
# function scope:
#

def f(message):
   def g():
      print(message)
   g()

f("Hello World!")

#
# Assigning to variables in the enclosing scope will produce
# a copy:
#

def f(number):
   def g():
      number = 2
   g()
   print(number)

f(1)                                         #  1, not 2

#
# Unless the inner function variable is declared nonlocal:
#

def f(number):
   def g():
      nonlocal number
      number = 2
   g()
   print(number)

f(1)                                         #  2

#
# Inner functions can still access variables in the parent
# function scope if the inner function is returned. This
# is called a closure.
#

def f(number):
   def g():
      print(number)
   return g

a = f(1)
a()                                          #  1

#
# To print a list of variables captured by the closure:
#

print(a.__closure__)

#
# If a function returns multiple closures, the variables
# captured by the closure can be shared:
#

def f(number):
   def g():
      nonlocal number
      number += 1
      print(number)
   def h():
      nonlocal number
      number += 2
      print(number)
   return (g, h)

a,b = f(1)
a()                                          #  2
b()                                          #  4, not 3
