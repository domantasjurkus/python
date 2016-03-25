x = str((17**39)**11)

sum = ''
for i in range(0, len(x), 33):
    print i
    sum += x[i]

print sum
