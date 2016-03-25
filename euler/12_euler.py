def tri(num):
    number = 0
    while num > 0:
        number += num
        num -= 1
    return number

def countDivs(num):
    primes = primeDict(num)
    expList = []
    for key in primes:
        expList.append(primes[key] + 1)
    return reduce(lambda x, y: x*y, expList)

# Function that returns factors and their exponents as a dictionary
def primeDict(numArg):
    num = numArg
    factor = 2
    finalDict = {}
    while num > 1:
        if num % factor == 0:
            num /= factor
            # if the factor has not yet been added
            if finalDict.get(factor, 0) == 0:
                finalDict[factor] = 1
            else:
                finalDict[factor] += 1
            factor = 1
        factor += 1
    return finalDict

i = 2
while True:
    triang = tri(i)
    divs = countDivs(triang)
    print triang, divs
    if divs > 500:
        print 'Answer:', triang
        break
    i += 1