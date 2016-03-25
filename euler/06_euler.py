# -*- coding: utf-8 -*-
# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of
# the first 100 natural numbers and the square of the sum.

# 1^2 + 2^2 + ... + n^2 = firstSum
firstSum = 0
# (1 + 2 + ... + n)^2 = secondSum
secondSum = 0
# count - number of iterations needed
count = 100

# Let's find firstSum... loop through (1,100)
for i in range(1, count+1):
    firstSum += i**2
print firstSum

# And now secondSum
for i in range(1, count+1):
    secondSum += i
secondSum = secondSum**2
print secondSum

print 'Sum difference:', secondSum, '-', firstSum, '=', secondSum-firstSum
