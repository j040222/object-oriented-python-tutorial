#
# Operator overloading:
#

class A:
   def __init__(self, value):
      self.value_ = value
   
   #
   # Overloaded arithmetical operators:
   #
   
   #
   # a + b:
   #
   
   def __add__(self, other):
      print("+")
      return A(self.value_ + other.value_)
   
   #
   # a - b
   #
   
   def __sub__(self, other):
      print("-")
      return A(self.value_ - other.value_)
   
   #
   # a % b:
   #
   
   def __mod__(self, other):
      print("%")
      return A(self.value % other.value_)
   
   #
   # a * b
   #
   
   def __mul__(self, other):
      print("*")
      return A(self.value_ * other.value_)
   
   #
   # a ** b:
   #
   
   def __pow__(self, other):
      print("**")
      return A(self.value_ ** other.value_)
   
   #
   # a / b
   #
   
   def __truediv__(self, other):
      print("/")
      return A(self.value_ / other.value_)
   
   #
   # a // b:
   #
   
   def __floordiv__(self, other):
      print("//")
      return A(self.value_ // other.value_)
   
   #
   # a << b:
   #
   
   def __lshift__(self, other):
      print("<<")
      return A(self.value << other.value_)
   
   #
   # a >> b
   #
   
   def __rshift__(self, other):
      print(">>")
      return A(self.value >> other.value_)
   
   #
   # a & b
   #
   
   def __and__(self, other):
      print("&")
      return A(self.value & other.value_)
   
   #
   # a | b
   #
   
   def __or__(self, other):
      print("|")
      return A(self.value | other.value_)
   
   #
   # a ^ b
   #
   
   def __xor__(self, other):
      print("^")
      return A(self.value ^ other.value_)
   
   #
   # ~a
   #
   
   def __invert__(self):
      print("~")
      return A(~self.value)
   
   #
   # Overloaded comparison operators:
   #
   
   #
   # a < b
   #
   
   def __lt__(self, other):
      print("<")
      return (self.value_ < other.value_)
   
   #
   # a > b
   #
   
   def __gt__(self, other):
      print(">")
      return (self.value_ > other.value_)
   
   #
   # a == b
   #
   
   def __eq__(self, other):
      print("==")
      return (self.value_ == other.value_)
   
   # 
   # a != b
   #
   
   def __ne__(self, other):
      print("!=")
      return (self.value_ < other.value_)
   
   #
   # a <= b
   #
   
   def __le__(self, other):
      print("<=")
      return (self.value_ <= other.value_)
   
   #
   # a >= b
   #
   
   def __ge__(self, other):
      print(">=")
      return (self.value_ >= other.value_)
   
   def __repr__(self):
      return str(self.value_)

a = A(1)
b = A(2)

print(a + b)                              #  + 3
print(b ** a)                             #  ** 2
print(a <= b)                             #  <= True
