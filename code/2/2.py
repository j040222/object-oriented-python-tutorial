#
# Select builtin functions:
#

#
# abs(x) returns the absolute value of an integer or a
# floating point number, the magnitude of a complex number,
# or x.__abs__, if it implements it:
#

class A:
   value_ = 1
   def __abs__(self):
      return 1

a = A()
print(abs(a))                             #  1

#
# all() compares all of the elements of an iterable to
# True. It returns False if at least one such test failed:
#

x = [ True, True, False ]
print(all(x))                             #  False

#
# any() compares all of the elements of an iterable to
# True. It returns False if all such tests failed:
#

print(any(x))                             #  True

#
# ascii is as repr, except that ascii() escapes all
# non-ASCII characters in the string returned by repr():
#

class A:
   value_ = 1
   def __repr__(self):
      return str(self.value_)

a = A()
print(ascii(a))                           #  1
print(repr(a))                            #  1

#
# bin(x) returns the binary representation of an integer,
# or the binary representation of x.__index__ if it exists
# and if it returns an integer:
#

class A:
   value_ = 1
   def __index__(self):
      return self.value_

a = A()
print(bin(a))                             #  0b1
# print(bin(1.0))                         #  floats not allowed

#
# bool returns a boolean by testing the truth value of its
# argument. An object is considered to be true unless its
# class defines __bool__ (returning False) or a __len__
# method that returns 0:
#

x = bool(True)
print(x)                                  #  True

class A:
   def __bool__(self):
      return False

a = A()
print(bool(a))                            #  False

#
# Enter the debugger (pdb) at this line, unless
# PYTHONBREAKPOINT=0 (a shell variable):
#

# breakpoint()                            #  Enter debugger

#
# A bytearray is an array of bytes. It is a mutable sequence
# of integers in the range 0 <= x <= 255. Being mutable, it
# supports slicing and array indexing.
#

primes = [2,3,5,7,11]
a = bytearray(primes)
print(a)

#
# To create a bytearray from a string you must specify the
# encoding:
#

a = bytearray("a string", "ascii")
print(a)
print(a[0])                               #  97

#
# bytes() creates an immutable bytearray:
#

a = bytes("a string", "ascii")
# a[0] = 98                               #  Disallowed

#
# callable returns True if an object appears to be callable.
# Otherwise it returns False. Classes are callable. Class
# instances are callable if they define __call__ (in which
# case they have operator()).
#

class A:
   def __call__(self):
      print("Callable")

a = A()
print(callable(A))                        #  True
print(callable(a))                        #  True: a() exists

#
# chr(x) returns the string representation of the unicode
# code point x. For example, chr(97) is 'a' (because the
# ascii code point of 'a' is 97).
#

print(chr(97))                            #  'a'

#
# @classmethod modifies class methods so that the first
# argument is the class, not 'self'. @classmethod functions
# can be called using only the class name (and also using
# instances):
#

class A:
   @classmethod
   def f(cls, x):
      print(x)

A.f(1)                                    #  1
A().f(1)                                  #  1

#
# compile() compiles a string (which may or may not come
# from a file) into executable code. Use exec() or eval()
# to execute the compiled code. Once executed, variables
# in the compiled code become variables in the calling code:
#

code = "x1 = 10\nprint(x)"
executable_code = compile(code, "<string>", "exec")
exec(executable_code)                     #  10
print(x1)                                 #  10

#
# Create the complex number 1 + i:
#

a = complex(1, 1)
print(a)

#
# Delete an attribute from a class. Note that deleting the
# attribute from the class also deletes it from all
# instances:
#

class A:
   value_ = 1

a = A()
delattr(A, "value_")
# print(a.value_)                         #  No such attribute

#
# Create and use a dictionary:
#

a = dict()                                #  Or a = {}
a["first"] = 2
print(a)
print(a["first"])

#
# dir() returns a list of names in a scope. Without
# arguments, it returns a list of names in the current local
# scope. With arguments, dir(x), it returns a list of 
# attributes for x.
#

print(dir())

class A:
   value_ = 1;

print(dir(A))

class A:
   def __dir__(self):
      return []

print(dir(A()))                           #  []

#
# divmod(a, b) takes two non-complex numbers as arguments
# and returns two numbers as follows: the quotient and the
# remainder of a / b.
#

print(divmod(10,3))                       #  (3, 1)
print(divmod(10.,3.))                     #  (3.0, 1.0)
print(divmod(10.,-3.))                    #  (-4., -2.)
                                          #  because -4*-3+-2=10

#
# enumerate() converts an iterator (or an iterable
# sequence, like an array) to an iterator that returns a
# tuple containing the count (starting at 0) and the value
# of the iterator at that index:
#

array = ["First", "Second", "Third"]
print(list(enumerate(array)))             #  [ (0, 'First') ... ]

for index, element in enumerate(array):
   print(index, element)                  #  Iteration

#
# eval() evaluates an expression and returns the result of
# the evaluation. It accepts 3 arguments as follows:
# eval(code, globals, locals).
#
# globals is a dictionary that specifies what variables and
# functions are available. If globals={}, only builtin
# functions are allowed in the evaluated expression.
#

import math
from math import *

print(eval("sqrt(9)"))                    #  OK - 3.0
# print(eval("sqrt(9)", {}))              #  Error, globals is {},
                                          #  so builtins only.
print(eval("sqrt(9)", {"sqrt":sqrt}))     #  3.0
a = 1
# print(eval("a=2"))                      #  Not allowed
                                          #  Cannot evaluate
                                          #  a statement

#
# exec() differs from eval() in that:
#
#     (a)   exec() can evaluate multiple lines and
#           statements
#     (b)   exec() always returns None
#

a = 1
exec("a=2")
print(a)                                  #  2

#
# filter(f, i) constructs an iterator from the elements e
# of an iterable i for which f(e) is true. If f is None,
# then the truthiness of e is tested instead:
#

a = [0, 1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : not (x % 2), a)))
                                          #  [0, 2, 4, 6, 8, 10]

#
# float constructs a floating point number, parses one
# from a string, or calls x.__float__:
#

a = float(1.0)                            #  1
a = float("1.0")                          #  1
a = float("Inf")
print(a)
a = float("INFINITY")                     #  case-insensitive
print(a)
print(float())                            #  0.0

class A:
   def __float__(self):
      return 1.0

a = A()
print(float(a))                           #  1.0

class A:
   def __index__(self):                   # Use __index__, if __float__
      return 1                            # is not present

a = A()
print(float(a))                           #  1.0

#
# format(x, s) returns a formatted representation of x.
# s is the format specification string. s accepts many
# options, see https://docs.python.org/3/library/string.html#formatspec.
#
# If x is a class object, then format() searches for
# x.__format__:
#

a = 1
print(format(x, '05b'))                   #  binary, with 5 figures

class A:
   value_ = 1
   def __format__(self, s):
      if s == "Integer":
         return str(self.value_)
      elif s == "Float":
         return str(float(self.value_))

a = A()
print(format(a, "Integer"))               #  1
print(format(a, "Float"))                 #  1.0

#
# A fronzenset is an immutable set object. It can be
# constructed from an iterable. If the iterable is a dict,
# only the keys of the dictionary are used.
#

a = ['a', 'b', 'c']
fs = frozenset(a)
print(fs)                                 #  frozenset({'a', 'b', 'c'})
# fs.add('f')                             #  Not allowed
a = { 'a':1, 'b':2, 'c':3 }
fs = frozenset(a)
print(fs)                                 #  The same

#
# getattr(object, name) returns the value of the attribute
# of object with name 'name'. 'name' must be a string.
# 
# If the required attribute exists, getattr(object, name)
# is equivalent to object.name.
#

class A:
   pass

a = A()
a.value_ = 1
print(getattr(a, "value_"))               #  1
print(getattr(a, "not_present_", 2))      #  Default value: 2

#
# globals() returns a dictionary containing the current
# global symbol table.
#

a = 1
globals()["a"] = 2
print(a)                                  #  2

#
# hasattr(object, name) checks whether object contains
# an attribute with name 'name':
#

class A:
   value_ = 1

a = A()
a.value2_ = 2
print(hasattr(a, "value_"))               #  True
print(hasattr(a, "value2_"))              #  True
print(hasattr(a, "value3_"))              #  False

#
# hash(x) returns the hash of x, if it has one. If x is
# an object, hash(x) checks for a __hash__ method which
# customizes the hash. Hashes are integers, truncated to
# bitwidth of the host machine.
#

print(hash(1))
print(hash( (1,2,3) ))                    #  Combined hash of tuple
                                          #  elements

#
# If __hash__ is customized then __eq__ should also be
# customized:
#

class A:
   value_ = 1
   def __eq__(self, other):
      return self.value_ == other.value_
   def __hash__(self):
      return hash(self.value_)

print(hash(A()))
print(hash(A().value_))                   #  The same

#
# help() and help(object) open a builtin interactive help
# system. If the argument is a string, then the help system
# looks for help pages for the specified module, function,
# class (and so on).
#

class A:
   pass

# help(A)                                 #  Open interactive help on A

#
# hex(o) converts an integer 'o' to a lowercase hex string.
# The string is prefixed with '0x'. If 'o' is not an
# integer, then hex(o) searches for o.__index__:
#

class A:
   def __index__(self):
      return 1

print(hex(A()))                           #  0x1

#
# id(x) gets the unique ID of an object x. Two objects with
# non-overlapping lifetimes may have the same id() value
#
# The ID of an object may differ between systems. The object
# to ID may be a class name, a class instance, a type, or
# a dict (among other objects):
#

print(id(10))
a = 10
print(id(a))                              #  The same

#
# input(x) gets a line from the console. It gets an input
# from the user and then returns it with the trailing
# newline character removed. If x is given, it is written
# to stdout without a trailing newline.
#

import readline                           #  Allows editing of the
                                          #  input string
# a = input("Enter a string <<< ")
print(a)

#
# int(x) instantiates an integer, x, or parses a string as
# an integer. If a second argument is given - int(x, b) -
# then x should be a string (or a bytearray) expressed in
# base b. The allowed bases are 0 and 2-36.
#
# If x is a floating point number, int(x) truncates toward
# zero. If x is an object, int(x) searches for __int__, then
# for __index__ (if __int__ is not present), then for
# __trunc__.
#

print(int())                              #  0
print(int(2.7))                           #  2
print(int(-2.7))                          #  -2

class A:
   def __int__(self):
      return 3
a = A()
print(int(a))                             #  3

print(int("0b1", 2))                      #  1
print(int('9', 36))                       #  9
print(int('a', 36))                       #  10
print(int('z', 36))                       #  35

#
# isinstance(o, c) checks whether o is an instance (or is a
# subclass) of a class type, c.
#
# c can be a tuple of typenames, in which case isinstance
# returns True if o is an instance of at least one of the
# tuple elements.
#

a = 3

print(isinstance(a, list))                #  False
print(isinstance(a, (list, int)))         #  True

#
# issubclass(c1, c2) checks whether c1 is a subclass of
# class type c2. A class is considered to be a subclass of
# itself.
#
# c2 can be a tuple of typenames, in which case issubclass
# returns True if c1 is a subclass of at least one of the
# tuple elements.
#

a = 3

print(issubclass(type(a), list))          #  False
print(issubclass(type(a), (list, int)))   #  True

class A:
   pass
class B(A):
   pass

print(issubclass(B, A))                   #  True

#
# iter(x) returns an iterator view of x. If x is an object,
# then x should implement __iter__ and __next__.
#
# iter(x, s) returns an iterator view of x, with sentinel
# s. Iteration is stopped when x() is s. In this case, x
# should be callable (Ie. it should implement __call__).
#

class A:
   def __init__(self):
      self.value_ = 0
   def __iter__(self):
      return self
   def __next__(self):
      if(self.value_ > 6):
         raise StopIteration
      value = self.value_
      self.value_ += 2
      return self.value_
   __call__ = __next__

a = A()
print(list(iter(a)))                      #  [2, 4, 6, 8]
print(list(iter(A(), 6)))                 #  [2, 4]

#
# len(x) returns the number of items comprising x. x can be
# a sequence (including strings) or a collection.
#
# If x is a custom object, len(x) calls x.__len__.
#

class A:
   def __len__(self):
      return 2

a = A()
print(len(a))                             #  2

#
# list() and list(iterable) create a mutable sequence type.
# Slicing and array access are both supported:
#

a = list()
a.append(1)
print(a)                                  #  [1]
a = list({"1":1, "2":2})
print(a)                                  #  Keys only: ['1', '2']

#
# locals() returns a dictionary containing the local symbol
# table:
#

def f(x):
   print(locals())                        #  { 'x':1 }
f(1)

#
# map(f, i) applies a function f to every element of an
# iterable, i, returning a new iterator containing the
# mapped results. If multiple iterables i1, i2 are
# provided - map(f, i1, i2...) - then f must accept that
# many arguments:
#

print(list(map(lambda x : 2*x, [1,2,3]))) #  [2, 4, 6]
a = map(lambda n1,n2:(n1 + n2), [1,2,3], [4,5,6])
print(list(a))                            #  [5, 7, 9]

#
# max(i) returns the largest element in an iterable i.
# max(x1, x2...) returns the largest element among objects
# x1, x2... . A default return value can also be specified
# for iterables.
#

print(max([1,2,3]))                       #  3
print(max(1, 2, 3))                       #  3
print(max([], default=3))                 #  3
a = {1:1,2:4}
print(max(a,key=lambda k:a[k]))           #  The key having the
                                          #  largest value, 2.

#
# min(i) returns the lowest element in an iterable i.
# min(x1, x2...) returns the lowest element among objects
# x1, x2... . A default return value can also be specified
# for iterables.
#

print(min([1,2,3]))                       #  1
print(min(1, 2, 3))                       #  1
print(min([], default=3))                 #  3
a = {1:1,2:4}
print(min(a,key=lambda k:a[k]))           #  The key having the
                                          #  lowest value, 1.

#
# next(o) gets the next item from an iterator o. It calls
# o.__next__, which raises a StopIteration exception when
# the iterator is exhausted. If a second argument is given,
# next(o, d), then d is returned when the iterator is
# exhausted:
#

a = iter([1])
print(next(a))                            #  1
a = iter([1])
next(a)
print(next(a, 2))                         #  2

#
# object() creates a basic object. object is a base class
# for all other classes. It contains methods that are common
# to all python classes:
#

a = object()
print(dir(a))

#
# oct() converts an integer to its octal representation. The
# string representation is prefixed with '0o'. If x is an
# object (not an int) then it must define __index__:
#

class A:
   def __index__(self):
      return 1
a = A()
print(oct(a))                             #  0o1
print(oct(0b1))                           #  0o1

#
# open(f) opens a file f for IO operations (which may
# include writing). There are many additional arguments (see
# https://docs.python.org/3/library/functions.html#open) for
# buffering, encoding, how encoding and decoding errors
# should be handled, and how to parse newline characters in
# the stream.
#

with open("./2.txt", 'r') as stream:
   line = stream.readline()
   print(line.strip())

#
# ord(x) returns the string representation of one unicode
# character x. This is the inverse function of chr():
#

print(chr(ord('€')));                     #  €

#
# pow(x, y) returns x raised to the power y. If a third
# argument is given, pow(x, y, b), then the returned value
# is x**y mod b. If x is negative and y is not an integer,
# a complex value is returned. If y is negative, b is given
# and all arguments are integers, then x must be relatively
# prime to mod and pow(x, y, b) = pow(x**-1, -y, b) where
# x**-1 is the inverse of x mod b.
#

print(pow(2, 3))                          #  8

#
# print(*x) prints the objects x to a text stream. By
# default the stream is ::std::cout. Use print(*x, sep, end)
# to specify the separator and terminator characters,
# respectively.
#
# To print to a custom object o, call print as follows
# print(*x, file=o), and implement o.write(self, string):
#

class A:
   def write(self, string):
      print(string, end='')

a = A()
print(1, file=a)                          #  1

#
# property(g, s, d, doc) creates a class property attribute
# out of a getter g, a setter s, and a deleter d. doc is
# a documentation string to assign to the property.
#
# Using property you can control the behaviour of
# expressions like x.name and del x.name, where x is the
# name of a property. You must specify the getter, the
# setter, and the deleter methods.
#

class A:
   def __init__(self, value):
      self._value = value
   def get_value(self):
      return self._value
   def set_value(self, value):
      self._value = value
   def del_value(self):
      del self._value
   value = property(get_value, set_value, del_value, "Value")

a = A(0)
print(a.value)                            #  a.get_value()
a.value = 1                               #  a.set_value(1)
print(a.value)                            #  1
del a.value                               #  a.del_value()

#
# Alternatively, using the @property decorator:
#

class A:
   def __init__(self, value):
      self._value = value
   @property
   def value(self):
      return self._value
   @value.setter
   def value(self, value):
      self._value = value
   @value.deleter
   def value(self):
      del self._value

a = A(0)
print(a.value)                            #  a.get_value()
a.value = 1                               #  a.set_value(1)
print(a.value)                            #  1
del a.value                               #  a.del_value()

#
# range(start, stop, step) constructs an immutable sequence
# type consisting of the elements from start (inclusive)
# to stop (exclusive) in steps of size step. Step must be
# an integer.
#

print(list(range(2)))                     #  [0, 1]
print(list(range(0, 2, 1)))               #  The same

#
# repr(x) returns a string containing a printable
# representation of an object x. In many cases the string
# representation will yield an object with the same value
# when passed to eval(). If x is a class, repr(x) calls
# x.__repr__:
#

class A:
   def __repr__(self):
      return '2'

a = A()
print(repr(a))                            #   '2'

#
# reversed(s) constructs a reverse iterator from a sequence
# s. s must provide s.__reversed__ (eg. arrays, ranges,
# tuples) or it must implement the sequence protocol:
# s.__len__ must exist, as well as s.__getitem__:
#

print(list(reversed([1,2,3])))            #  [3,2,1]
print(list(reversed(range(1,4))))         #  The same
print(list(reversed((1,2,3))))            #  The same

class A:
   arr_ = [1,2,3]
   def __len__(self):
      return len(self.arr_)
   def __getitem__(self, index):
      return self.arr_[index]

a = A()
print(list(reversed(a)))                  #  [3,2,1]

#
# round(x, n) rounds x to n digits after the decimal point.
# If n is not given (or is None), it rounds to the nearest
# integer. If x is half way between the nearest rounded
# values, it is rounded toward the even choice. If x is
# an object, round() delegates to x.__round__:
#

class A:
   number_ = 1.5
   def __round__(self):
      return round(self.number_)

a = A()
print(round(a))                           #  2

#
# set() constructs a mutable version of a frozenset. If an
# iterable x is given, set(x) is populated with the items in
# x:
#

a = set([1,2])
print(a)                                  #  {1,2,3}
b = set([1,2,3])
print(a < b)                              #  True: a is contained
                                          #  in b

#
# setattr(object, name, value) is equivalent to
# object.name = value. Note that object can be a class name
# or an instance:
#

class A:
   pass
setattr(A, "value_", 1);
a = A()
print(a.value_)

#
# slice(stop) and slice(stop, start, step) return slice
# objects that can be used to slice any sequence. stop,
# start, step must all be integers. Note that all three
# arguments can be negative, in which case slicing starts
# at the end of the string and works backwards.
#
# Slice objects contain attributes named stop, start and
# step with the same value as the arguments.
#

indices = slice(2)
a = [1,2,3]
print(a[indices])                         #  [1,2]
print(indices.stop)
indices = slice(-1,-3,-1)
print(a[indices])                         #  [3,2]

#
# Alternatively, use extended indexing syntax:
#

print(a[-1:-3:-1])                        #  The same

#
# sorted(x, key=None, reverse=False) constructs a new list
# containing the sorted values of an iterable x. If key
# is specified then it should be a univariate function that
# extracts a comparison key from each element in x. The sort
# is stable.
#

a = [1,3,2]
print(sorted(a))                          #  [1,2,3]
a = [(1,2),(2,1)]
print(sorted(a,key=lambda x : x[1]))      #  Sort by the second
                                          #  tuple element

#
# @staticmethod transforms a class method into a static
# method. Static methods have no implicit 'self' argument.
# (nor do they have implicit class name arguments, like
# @classmethod).
#

class A:
   @staticmethod
   def f(x):
      return (x + 1)

a = A()
print(a.f(1))                             #  2
print(A.f(1))                             #  2

#
# str(x) returns a string representation of x. If x is
# an integer, float or complex then str(x) is a string
# that parses to the same value.
#

print(complex(str(complex(1,1))))

#
# If x is a bytes object, or a bytearray object, then
# str(x, encoding='utf-8', errors='strict') accepts two
# additional arguments that specify the byte encoding and
# what to do if an invalid encoded character is detected:
#

a = [112, 121, 116, 104, 111, 110]        # "python"
a = bytes(a)
print(str(a, encoding='utf-8'))           # "python"

#
# sum(x, start=0) sums the items of an iterable and returns
# the total value. If start is given, it is added to the 
# total.
#

print(sum([1,2,3]))
print(sum([1,2,3],start=1))               #  2+3=5

#
# To sum floating-point iterables with extended precision,
# use math.fsum instead:
#

import math
print(math.fsum([0.5, 1.5]))              #  2.0

#
# super() has two main use cases. Firstly, it removes the
# need to name a base class explicitly (for example during
# ctor evaluation):
#

class A:
   def __init__(self, x):
      print("A")
      self.x = x
class B(A):
   def __init__(self, x):
      print("B")
         #
         # Returns a proxy object that delegates to the
         # methods in A:
         #
      super().__init__(x)
      # Alternatively: A.__init__(self, x)

b = B(1)                                  #  B A

#
# Secondly, it chains multiply-inherited classes together
# according to their __mro__ (method resolution order). The
# __mro__ that is evaluated belongs to the instantiated
# class, not to the base class (which, on its own, will may
# have a different __mro__).
#
# super() with no arguments only works inside of a class
# definition. The compiler fills in the necessary missing
# arguments. This means that super(type, object_or_type) can
# be used outside of a class definition. In this form,
# if object_or_type is an instance, then super() generates
# a proxy for the next object in the __mro__ of
# object_or_type after type.
#
# You cannot use indexed expressions like super()[name]
# with super(): only dotted attribute lookups.
#

class A:
   def __init__(self, x):
      print("A")
      self.x = x
class B(A):
   def __init__(self, x):
      print("B")
      super().__init__(x)                 # Same as super(B, self)
class C(A):
   def __init__(self, x):
      print("C")
      super().__init__(x)                 # Same as super(C, self)
   def f(self):
      print("f")
   @staticmethod
   def g():
      print("g")
class D(C, B):
   def __init__(self, x):
      print("D")
      super().__init__(x)

d = D(1)                                  #  D C B A

super(D, d).f()                           #  "f"
super(D, D).g()                           #  Allowed - "g"

#
# tuple() and tuple(iterable) are immutable sequence types.
# Tuples support indexing and slicing.
#

a = tuple([1,2,3])
print(a[1:3])                             #  (2,3)

a = (1,2) + (3,4)
print(a)                                  #  (1,2,3,4)

a = (1,2)*3
print(a)                                  #  (1,2,1,2,1,2)

print((1,2,1).count(1))                   #  2

#
# type(x) returns the type of x, which is usually the same
# as x.__class__.
#
# type(name, bases, dict) creates a new type, even it has
# not been previously declared as a class. In this case
# name becomes the __name__ attribute, bases becomes the
# __bases__ attribute, and dict contains definitions for
# the class body and becomes the __dict__ attribute. This
# form is essentially a dynamic form of the 'class'
# statement. If bases is empty then 'object' is
# automatically added to it.
#

a = 1
print(type(a))                            #  int

del B
del A
a = type('A', (), {'value_':1})
print(a.value_)                           #  1

#
# vars(x) returns the __dict__ attribute for any object
# (or module) that has it, otherwise it raises a TypeError.
# vars() (no arguments) returns methods in the local scope.
#

print(vars(tuple))
print(tuple.__dict__)                     #  The same

#
# zip(*iterables, strict=False) iterates over several
# iterables in parallel. It produces tuples containing one
# item per iterable. The zip iterator is as long as the
# shortest iterable, unless strict=True, in which case
# a ValueError is raised if the iterables do not have the
# same length.
#

print(list(zip([1,2], (3,4,5))))          #  [(1, 3), (2, 4)]
a = [1,2]
b = [3,4]
c = list(zip(a, b))
a, b = zip(*c)                            #  a = (1,2) b = (3,4)
print(a,b)
