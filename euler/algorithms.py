from math import sqrt

# Get a list of divisors for the given number
def getDivisors(n):
    divisors = [1]
    for i in xrange(2, int(sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if n/i != i:
                divisors.append(n/i)

    return divisors

