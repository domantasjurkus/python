#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#abc x def = palindrome
#999 x 999 = 998001 (largest number made from two 3-digit numbers)

def isPal(num):             #function for checking whether a number is palindromic

    #first of all, let's be sure the number is actually an integer
    #if the number 'num' is NOT an instance of 'int'...
    if isinstance(num, int) == False:
        return False        #that's what you get for passing a float

    #now if the number is just a single digit - it's palindromic by default
    if num < 10:
        return True

    #Now if the number has 2+ digits...
    digits = 1              #first, we need to find out how many digits our number has
    a = 1                   #a - variable for checking, will become 10, 100, 1000, ...
    while a <= num:         #while our number has more digits that our checker variable...
        a = a*10            #keep expanding our checker variable
        digits += 1         #and count how many times we've expanded
    digits -=1              #we will always expand one time too much

    bigInd = digits         #assuming our number is an array starting with 1, let's note
    smaInd = 1              #the biggest and smallest indexes
    
    #if there is an odd number of digits, this loop will ignore the middle digit
    for i in range(digits/2):
        #print '-----iteration'
        #print 'Big digit index:', bigInd
        #print 'Small digit index:', smaInd

        #we will first compare the biggest and the smallest digits,
        #then the 2nd biggest and 2nd smallest, and so on
        #print 'Current largest number:', num/(10**(bigInd-1))%10
        #print 'Current smallest number:', (num%(10**(smaInd)))/10**(smaInd-1)

        #You'll have to trust me on this one - the long complicated lines
        #get the current biggest and smallest digits that we're checking.
        #So if those digits are equal...
        if num/(10**(bigInd-1))%10 == (num%(10**(smaInd)))/10**(smaInd-1):
            
            if bigInd == smaInd:            #and if the indexes have reached each other
                return True
            elif bigInd == smaInd + 1:      #or if they're just 1 step appart (even number)
                return True
            
            #print '*', bigInd, 'and', smaInd,'digits are equal.'
            bigInd -= 1                     #we increment/decrement the indexes
            smaInd += 1                     #of the values we're checking

    return False

#And now, just count downwards from 998001 until we hit the first palindrome
a = 999

#Hopefully we'll find the digit by multiplying everything between 999 and  950
while a > 950:
    
    b = 999
    while b > 900:
        #print 'a', a, 'b', b  
        if isPal(a*b) == True:
            print 'Pal:', a*b
        b -= 1
    a -= 1
