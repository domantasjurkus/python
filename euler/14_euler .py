# recursive algorythm
def chainLength(num):
	if num == 1:
		return 1
	else:
		if num % 2 == 0:
			return 1 + chainLength(num/2)
		else:
			return 1 + chainLength(num*3 + 1)

# looping algorythm
def func(numArg):
	num = numArg
	length = 1
	while num > 1:
		if num % 2 == 0:
			num /= 2
		else:
			num = num * 3 + 1
		length += 1
	return length

longestChain = 0
longestArg = 0
i = 1000000
while True:
	length = func(i)
	if longestChain < length:
		longestChain = length
		longestArg = i
	i -= 1
	if i == 1:
		print longestArg
		print longestChain
		break
