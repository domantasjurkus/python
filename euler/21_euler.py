def getProperDivs(n):
	list = [1]
	if n < 1:
		return []
	elif n == 1:
		return list

	for i in range(2, n):
		if n%i == 0:
			list.append(i)
	return list

def getListSum(list):
	return reduce(lambda x, y: x+y, list)

foundNums = []

for i in range(2, 10000):
	l = getProperDivs(i)
	s = getListSum(l)
	if i == s:
		continue

	l2 = getProperDivs(s)
	s2 = getListSum(l2)
	print i, l, s, s2
	if s2 == i:
		# print "--^--amicable--^--"
		if i not in foundNums:
			foundNums.append(i)
		if s2 not in foundNums:
			foundNums.append(s2)

print foundNums

print reduce(lambda x,y: x+y, foundNums)