

#
# To create a generator, use the 'yield' keyword as follows.
# Functions that yield values can be called like iterators.
#
# The generator will be evaluated up until the
# first yield statement, then it will suspend until it it
# called again.
#
# Generators can be more memory efficient than class
# iterators. Generators only evaluate the items they
# return when they are called.
#

def generator(n):
   counter = 0
   while(counter < n):
      yield counter
      counter += 1

print(generator(2))                          #  Not 0

#
# A for loop can be used to extract values from generators:
#

for value in generator(4):
   print(value)                              #  0 1 2 3

#
# Alternatively:
#

g = generator(2)
print(next(g))                               #  0
print(next(g))                               #  1

#
# The elements returned by generators (and by iterators) can
# be modified using the following syntax:
#
#     (expression for item in generator):
#

squares = (i * i for i in generator(3))
for i in squares:
   print(i)                                  #  0 1 4

#
# Generators can also be combined into 'pipelines' as
# follows:
#

def generator(n):
   counter = 0
   while(counter < n):
      yield counter
      counter += 1
def square(gen):
   for item in gen:
      yield item * item

print(max(square(generator(4))))             #  9
