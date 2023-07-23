
#
# Decorators are functions that modify other functions. The
# decorator accepts one argument - the function to modify -
# and returns another function - the modified function. This
# is typically done using a closure:
#

def prefix_log_message(delegate):
   def function(message):
      print("log: ")
      delegate(message)
   return function

@prefix_log_message
def log(message):
   print(message)

log("Hello World!")

#
# Decorators can be chained together. The most inner
# decorator (in this example, '@square') is evaluated first.
#

def add_one(delegate):
   def function(n):
      return (delegate(n) + 1)
   return function

def square(delegate):
   def function(n):
      value = delegate(n)
      return (value * value)
   return function

@add_one
@square
def identity(n):
   return n

print(identity(1))                        #  1**2 + 1 = 2
print(identity(2))                        #  2**2 + 1 = 5
