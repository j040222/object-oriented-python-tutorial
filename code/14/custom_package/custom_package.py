
def increment_number(x):
   """Increment the input number by 1"""
   return (x + 1)

import argparse
from argparse import RawTextHelpFormatter

if __name__ == '__main__':
   
   #
   # Parse arguments:
   #
   
   parser =                                                \
      argparse.ArgumentParser                              \
         (
         formatter_class=RawTextHelpFormatter
         )
   
   parser.add_argument                                     \
      (
      "--input",
      type=int,
      required=True,
      help="The integer to increment"
      )
   
   args = parser.parse_args()
   
   input_number = args.input
   
   print(increment_number(input_number))
   
   exit(0)
