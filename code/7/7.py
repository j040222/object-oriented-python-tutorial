
#
# Property attributes allow you to customize the behaviour
# of attribute get/set expressions like a.value = (object):
#

class A:
   def __init__(self):
      self.value = 1

a = A()
a.value = 2                # Internally equivalent to
                           # a.__dict__['value']

#
# Now make value private and implement a getter and a
# setter for it:
#

class A:
   def __init__(self):
      self._value = 1
   def get_value(self):
      return self._value
   def set_value(self, value):
      self._value = value

#
# The above is not backward-compatible with the syntax
# a.value = (number). To make it compatible, use a property
# attribute as follows:
#

#
# Making _value a property attribute:
#

class A:
   def __init__(self):
      self._value = 1
   def get_value(self):
      return self._value
   def set_value(self, value):
      self._value = value
   value = property(get_value, set_value)

a = A()
a.value = 2
print(a._value)

#
# Using the @property decorator the same code can be
# accomplished as follows. Note that the setter function,
# value(self,value), below, cannot be named set_value:
#

class A:
   def __init__(self):
      self._value = 1
   @property
   def value(self):
      return self._value
   @value.getter
   def value(self):
      return self._value
   @value.setter
   def value(self, value):
      self._value = value

a = A()
a.value = 2
print(a.value)
