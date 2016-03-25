finalSum = 0                            #'sum' is taken, so let's use 'finalSum'

for i in range(1000):                   #go through all the numbers from 0 to 999
    if ((i%3==0)or(i%5==0)):            #if i divisible by 3 or by 5
        finalSum = finalSum + i         #add i to finalSum
print "1 + 2 + 3 + ... + 998 + 999 =", finalSum
