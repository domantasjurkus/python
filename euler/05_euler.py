# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive
# number that is evenly divisible by all numbers from 1 to 20?

#the number we're searching has factors that form the numbers 1->20
#so, we have to find all of these factors

# function for finding all factors of 'num'
def fac(fList, numArgument):

    # make a local copy of the argument
    num = numArgument
    print '-----Factors of', num

    # divider = posible factor
    divider = 2

    # while divider is less than the number
    while divider <= num:

        # if we divide with no remainder - we've found a factor
        if num % divider == 0:
            
            print divider

            # only if num cannot be formed without the factor
            # that we just found do we add divider to fList
            if canBeFormed(num) == False:
                addFactor(fList, divider)
                print 'Added:', divider

            # remove the factor from our number
            num = num / divider

            # reset divider to 1
            divider = 1

        # divider will increment by one,
        # and after finding a factor it will become 2 again
        divider += 1
                                            
# can we form numArgument from the current factors in fList?
def canBeFormed(numArgument):
    
    num = numArgument
    length = len(fList)

    divider = 2

    # loop through all the current factors
    for i in range(length):

        # if we find a factor, divide num by it
        if num % fList[i] == 0:
            num = num / fList[i]

    if num == 1:
        return True
    else:
        return False

# function for adding new factors to fList
def addFactor(fList, num):
    fList += [num]


number = 1
# list of factors
fList = [1]


for number in range(1, 21):
    fac(fList, number)

sum = 1

for i in range(len(fList)):
    sum *= fList[i]

print 'Answer:', sum
