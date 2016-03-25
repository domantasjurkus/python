# Find Pythagorean triplet for which a*b*c = 1000

for c in range(100, 500):
    for b in range(4, 500):
        for a in range(b, 500):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print a, b, c
    print 'Finished with c:', c
