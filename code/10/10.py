#
# Serialization is sometimes called marshalling or
# (in python) 'pickling'.
# Deserialization is sometimes called unmarshalling or
# (in python) 'unpickling'.
#

#
# There is more than one type of serialization in the
# python standard library. Examples include json (which
# converts objects to textural JSON and back), XML (the
# same, in XML format) and pickle (which converts objects
# to a binary format and back, using a deep copy).
#

#
# There is more than one pickle protocol for serialization.
# As of Python 3.8, there are 6 protocols. Higher versions
# of the python interpreter use higher pickle protocol
# versions by default. This means that pickles on one system
# are not necessarily fully compatible with other systems
# that use different protocol versions.
#

#
# Pickle cannot serialize lambda functions, and it cannot
# serialize many active objects like database connections
# and threads. Neither can json. Never unpickle from an
# untrusted source.
#

import pickle

class A:
   number_ = 1
   string_ = "Hello World!"
   dict_ = { 'first':1, 'second':2 }
   list_ = [1, 2]
   tuple_ = (1, 2)

a = A()
pickled = pickle.dumps(a)
b = pickle.loads(pickled)
a.number_ = 2
print(b.number_)                             # b != a

#
# dill is an alternative serializer that can serialize
# objects like nested functions and lambda functions. Dill
# can also serialize an entire interpreter session and
# subsequently reload it:
#

import dill
dill.dump_session("10.pkl");
# dill.load_session("10.pkl");

#
# To exclude an attribute from pickling, use __getstate__.
# __getstate__ should copy the object's __dict__ and remove
# any items for exclusion. Use __setstate__ to restore
# the missing items.
#

class A:
   def __init__(self):
      self.number_ = 1
      self.function_ = lambda x : (x + 1)
   
   #
   # Without this, pickle cannot serialize the above lambda
   # function.
   #
   
   def __getstate__(self):
      attributes = self.__dict__.copy()
      del attributes['function_']
      return attributes
   
   def __setstate__(self, deserialized_state):
      self.__dict__ = deserialized_state
      self.function_ = lambda x : (x + 1)

a = A()
pickled = pickle.dumps(a)
b = pickle.loads(pickled)
print(b.function_(1))                        #  2

#
# json can also be used to serialize some objects:
#

import json

class A:
   def __init__(self):
      self.number_ = 1
      self.string_ = "Hello World!"
      self.dict_ = { 'first':1, 'second':2 }
      self.list_ = [1, 2]
      self.tuple_ = (1, 2)

a = A()
a.number_ = 2

serialized = json.dumps(a.__dict__)
print(serialized)
b = A()
b.__dict__ = json.loads(serialized)
print(b.number_)                             #  2
