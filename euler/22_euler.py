file = open("22_data.txt",  "r")
data = file.readline().split(",")
list = map(lambda x: x[1:-1], data)
list.sort()
# print list
sum = 0


for i in xrange(len(list)):
	name = list[i]
	positionScore = i + 1
	nameScore = 0
	for char in name:
		nameScore += ord(char) - 64

	finalScore = positionScore*nameScore
	sum += finalScore

print sum