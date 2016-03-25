from math import *

def isPrime(num):
    if num == 1:
        return False
    elif num < 4:
        return True;
    elif num%2 == 0:
        return False;
    elif num < 9:
        return True
    elif num%3 == 0:
        return False
    else:

        r = floor(sqrt(num))
        f = 5
        while f <= r:
            if num%f == 0:
                return False
            if num%(f+2) == 0:
                return False
            f += 6

    return True

limit = 2000000
candidate = 3
sum = 2

while candidate < limit:
    if isPrime(candidate):
        sum += candidate
    candidate += 2
print sum
