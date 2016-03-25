'''
All integers greater than 28123 can be written as the sum of two abundant numbers.
'''

import math
from algorithms import getDivisors



def isNumberPerfect(num):
    if num == 1:
        return False
    list = getProperDivisors(num)
    sum = reduce(lambda x,y: x+y, list)

    return sum == num

def isNumberAbundant(num):
    list = getDivisors(num)
    sum = reduce(lambda x,y: x+y, list)

    return sum > num

# Main program (to keep global scope clean)
def main():
    MAX = 28124
    ab_sum = [False] * MAX
    div_sum = 0
    sum = 0

    # Get a list of abundant numbers up to 28123
    for i in xrange(1, MAX):
        div_sum = 0
        sum += i
        for e in xrange(1, i):
            if (i%e == 0):
                div_sum += e

        if div_sum > i:
            ab_sum[i] = True

    for i in xrange(i, MAX):
        for e in xrange(1, i):
            if ab_sum[e] and ab_sum[i-e]:
                sum -= i
                break

    print sum


# main()
