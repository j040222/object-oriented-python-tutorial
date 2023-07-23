#
# When calling a function, arguments can be specified using
# their names in the function signature:
#

def f(first, second):
   print(first, second)

f(first="Hello", second="World!")         #  "Hello World!"

#
# Keyword arguments can be specified in any order:
#

f(second="World!", first="Hello")         #  The same

#
# Keyword arguments must follow positional arguments:
#

f("Hello", second="World!")               #  "Hello World!"

#
# *args will give all positional arguments as a tuple:
#

def f(*args):
   for arg in args:
      print(arg, end=' ')
   print()

f("Hello", "World!")                      #  "Hello World!"

#
# ** will give all keyword arguments as a dict:
#

def f(**args):
   for key, value in args.items():
      print(value, end=' ')
   print()

f(first="Hello", second="World!")         #  "Hello World!"

#
# Both can be combined:
#

def f(arg0, arg1, *args, **kwargs):
   print(arg0, arg1, args, kwargs)
   print()

f("Hello", "World!", "This", "is", first="Mars")
            #  Hello World! ('This', 'is') {'first': 'Mars'}

#
# * and ** can also be used when calling functions. In this
# case, * unpacks a list or a tuple and ** unpacks a dict
# into an array of keyword arguments:
#

def f(*args):
   for arg in args:
      print(arg, end=' ')
   print()

f( *["Hello", "World!"] )                 #  "Hello World!"
f( *("Hello", "World!") )                 #  "Hello World!"

def f(**args):
   for key, value in args.items():
      print(value, end=' ')
   print()

f( **{ 'first':"Hello", 'second':"World!" } )

#
# In python3, * can also be used on the left hand side of
# an assignment operation. For example:
#

first, *others = [1,2,3]
print(others)                             #  [2,3]

#
# * can also be used by itself in a function argument list.
# In this case it means that all arguments after the *
# must be keyword (named) arguments:
#

def f(first, second="World!", *, rest):
   print(first, second, rest, end='')
   print()

f("Hello", rest="This is Mars")

#
# The return value of functions can be annoted using ->
# as follows:
#

def f(x) -> "The same value as the input":
   return x

#
# The annotation following -> can be accessed using
# f.__annotations__['return']:
#

print(f.__annotations__)

#
# The annotation need not be a string:
#

def f(x) -> { 'doc':"The same value as the input", 'type':int } :
   return x

print(f.__annotations__['return'])


