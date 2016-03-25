last = 1                                #last fibonacci term
fib = 2                                 #current fibonacci term
temp = 0                                #temporary placeholder

finalSum = 2                            #2 is even-valued, we have to add it manually here

while fib <= 4000000:                   #while the number hasn't got to 4 million

    temp = fib                          #before counting a new fibonacci, we have to preserve the current term
    fib = fib + last                    #current term - sum of last two terms
    last = temp                         #now, the last term is saved
   
    if fib > 4000000:                   #if we've reached 4 million - break
        print 'Fib is more than 4 mil. - breaking'
        break
    
    if fib%2==0:                        #if the current term is even-valued
        finalSum = finalSum + fib       #add it to the sum

    print 'Current term:', fib
    print 'Current sum:', finalSum

