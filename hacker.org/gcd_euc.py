import math

def gcd_euc(a, b):
	if a < b:
		temp = a
		a = b
		b = temp

	# a = b*q + p
	q = int(math.floor(a/b))
	p = int(a - b*q)

	# print a, "=", b, "*", q, "+", p

	if p > 0:
		return gcd_euc(b, p)
	else:
		return b

a = 100
b = 15
print gcd_euc(a, b)