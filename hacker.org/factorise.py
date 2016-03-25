from math import *

def gcd_euc(a, b):
	if a < b:
		temp = a
		a = b
		b = temp

	# a = b*q + p
	q = int(floor(a/b))
	p = int(a - b*q)

	# print a, "=", b, "*", q, "+", p

	if p > 0:
		return gcd_euc(b, p)
	else:
		return b

def largest_factor(n):
	if n % 2 == 0:
		lastFactor = 2
		n = n/2
		while n % 2 == 0:
			n = n/2
	else:
		lastFactor = 1
	factor = 3

	maxFactor = sqrt(n)

	while n > 1 and factor <= maxFactor:
		if n % factor == 0:
			n = n/factor
			lastFactor = factor
			while n % factor == 0:
				n = n/factor
			maxFactor = sqrt(n)
		factor += 2

	if n == 1:
		return lastFactor
	return n

print 7393913335919140050521110339491123405991919445111971/313