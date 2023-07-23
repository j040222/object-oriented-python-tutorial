#
# Lists can be created and populated with the following
# syntax:
#
#        (expression) (x) for x in (iterable)
#        
#        or:
#        
#        (expression) (x) for x in (iterable) if (condition)
#

a = [ 1,2,3,4,5,6 ]
b = [ x for x in a ]                      #  The same as a
print(b)

b = [ x for x in a if x % 2 == 0 ]        #  Even entries only
print(b)

#
# Tuples and other iterables can also be used:
#

a = ( 1,2,3,4,5,6 )
b = [ x for x in a if x % 2 == 0 ]        #  Even entries only
print(b)

#
# List comprehension can also be used to map list values:
#

a = 'abc'
b = ''.join( [ x.upper() for x in a ] )   #  Capitalize entries
print(b)                                  #  ABC

#
# Note that (expression) can also contain a condition:
#

a = 'abcdef'
b = ''.join( [ x.upper() if ord(x) % 2 == 0 else x for x in a ] )
                                          #  Capitalize every other
                                          #  letter
print(b)                                  #  aBcDeF

#
# Dictionaries can also be created and populated using the
# following syntax:
#
#        (key) : (value) for x in (iterable)
#        
#        or:
#        
#        (key) : (value) for x in (iterable) if (condition)
#

a = { 'first':1, 'second':2, 'third':3, 'fourth':4 }
b = { k:v for (k,v) in a.items() if v % 2 == 0 }
print(b)                                  #  Even values only

#
# Multiple if conditions are allowed:
#

b = { k:v for (k,v) in a.items() if v % 2 == 0 if v < 3 }
print(b)                                  #  {'second': 2}

#
# A custom context manager (for use with the 'with' keyword)
# can be created as follows. Declare a class with an
# __enter__ and an __exit__ function:
#

class A:
   def __enter__(self):
      print("initializing");
   def __exit__(self, type, value, traceback):
      print("closing")

with A() as a:
   print("working")

#
# a.__enter__ is called when the context manager is
# initialized (before "working"). __exit__ is called when
# the context manager terminates (after "working"). If an
# exception occurs, __exit__ receives the type, value and
# traceback of the exception as arguments:
#

import traceback

class A:
   def __enter__(self):
      print("initializing");
   def __exit__(self, type, value, traceback):
      #
      # Type: RuntimeError, value: the exception object,
      # traceback: a traceback at the exception site.
      #
      print(type, value, traceback)
      print("closing")
      #
      # If __exit__ returns True, the exception is captured
      # and the with statement will terminate normally. In
      # this case, the exception is 'handled':
      #
      return True

with A() as a:
   print("working")
   raise RuntimeError("exception")

#
# Context managers can also be created using contextlib and
# the @contextmanager decorator:
#

from contextlib import contextmanager

@contextmanager
def create_cm():
   value = 1
   try:
      yield value
   finally:
      pass

with create_cm() as a:
   print(a)                                  #  1
