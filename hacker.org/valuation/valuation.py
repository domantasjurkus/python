str = '93752xxx746x27x1754xx90x93xxxxx238x44x75xx08750912738x8461x8759383xx328x4x4935903x6x5550360535004x0xx945958961296x267x8842xxx5x6xx61x4x48482x80xxx83316843x7x4x83x9521731xxx25x51xx457x6x5x9698222x771237745034x5133592x27xx8x87xx35221x36x0x50x23x7x63x998418xx'
sum = 0
ind = 0

while True:
    last_ind = len(str)-1
    print "char: " + str[ind] + " index:", ind

    if str[ind] != 'x':
        sum += int(str[ind])
        ind += 1

    elif str[ind] == 'x':
        str = str[:ind] + str[ind+1:]
        ind -= 2

    if ind == last_ind:
        break

print sum
