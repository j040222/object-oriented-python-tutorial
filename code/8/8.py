#
# In a sense, coroutines are the opposite of generators.
# Generators produce data whereas coroutines consume data.
#
# When a coroutine is called for the first time, nothing
# happens. The coroutine only advances to the field yield
# statement when coroutine.__next__ or next(coroutine)
# is called. At this point execution is suspended until
# coroutine.send(data) is called. data is inserted at the
# position of the (yield) keyword.
#

def echo(modifier):
   while True:
      message = (yield)
      modified_message = modifier(message)
      print(modified_message)

coroutine = echo(lambda x : "log: " + x)

#
# Advance to the first 'yield' expression:
#

next(coroutine)

coroutine.send("Hello")                   #  log: Hello
coroutine.send("World!")                  #  log: World!

#
# Coroutines can run indefinitely: they can accept an
# indefinite number of send() operations. A coroutine can be
# closed by calling coroutine.close(). This raises a
# GeneratorExit exception, which the coroutine can capture:
#

def echo(modifier):
   try:
      while True:
         message = (yield)
         modified_message = modifier(message)
         print(modified_message)
   except GeneratorExit:
      print("closing coroutine")

coroutine = echo(lambda x : "log: " + x)

next(coroutine)

coroutine.send("Hello")                   #  log: Hello
coroutine.send("World!")                  #  log: World!
coroutine.close()                         #  "closing coroutine"

#
# Coroutines can be chained together into pipelines:
#

def producer(message, next_coroutine):
   next(next_coroutine)
   lines = message.split("\n")
   for line in lines:
      next_coroutine.send(line)
   next_coroutine.close()

def add_prefix(next_coroutine):
   next(next_coroutine)
   try:
      while True:
         message = (yield)
         next_coroutine.send("log: " + message)
   except GeneratorExit:
      pass

def state_message_len():
   try:
      while True:
         message = (yield)
         print(message + " (" + str(len(message)) + ")")
   except GeneratorExit:
      pass

producer("Hello\nWorld!", add_prefix(state_message_len()))
