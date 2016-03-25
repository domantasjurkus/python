from math import *

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

sum = 2

for num in xrange(2, 2119):
    if is_square(num):
        sum += num*2
    else:
        sum += num

print sum
