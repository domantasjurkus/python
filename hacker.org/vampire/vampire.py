f1 = open("original.txt", "r")
f2 = open("challenge.txt", "r")

caps = "QWERTYUIOPASDFGHJKLZXCVBNM"

l1 = f1.readline().split()
l2 = f2.readline().split()

for i in xrange(len(l1)):
    if l1[i] != l2[i]:
        if l2[i][0] in caps:
            print l2[i]

f1.close()
f2.close()
