# IMPORTING LIBRARIES

import math
print(math.log(8))
print(math.factorial(5))
print(math.pow(2,9))
print(math.sin(45))
a=math.factorial(6)
print(a)

# importing random variables in between 0 and 5
import random
a=print(random.random())

# tossing a coin problem using random library
import random
a=random.random()
if (a>0.5):
  print('Heads')
else:
  print('Tails')

# simulating a dice 
import random
print(random.randrange(1,7))

# simulating truth or dare
import random
choice=random.random()
if(choice>0.5):
  print('truth')
else:
  print('Dare')

# There are different ways to import libraries in python

import calendar
print(calendar.month(2025,1))
print(calendar.calendar(2025))

from calendar import *
print(month(2025,1))
from calendar import month
print(month(2025,5))

import calendar as c
print(c.month(2025,7))
