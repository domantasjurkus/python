'''
1. Bacteria is born from mother
2. Bacteria divides into two
3. Bacteria divides into two
4. -
5. Bacteria dies
'''

b1 = 1      # bacteria that was just born
b2 = 0      # bacteria that has split once
b3 = 0      # bacteria that has split twice
b4 = 0      # bacteria ready to die
total = 0

day = 1
while total < 1000000000000:
    
    # 2nd and 3rd day bacteria give birth
    b1 += b2
    b1 += b3
    total = b1+b2+b3+b4

    print "Day", day, "-", b1, b2, b3, b4, "Total -", total

    # end of day - shift bacteria groups
    # b4 dies
    b4 = b3
    b3 = b2
    b2 = b1
    b1 = 0

    day += 1