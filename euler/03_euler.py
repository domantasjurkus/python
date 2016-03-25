num = 600851475143                                #number we're checking
i = 1                                   #variable for iteration
prime = 2

def isPrime(num):
    j = 2
    while j < num:
        if num%j==0:
            return False
        j = j+1
    return True

#let's find all the factors of num
while i <= num:                         #let's go through all the numbers from 2 to num
    if (isPrime(i) and (num%i==0)):     #if the current number is prime AND it's a factor of num
        print i
        prime = i

    i += 2                              #increment by 2 in order to dogde even numbers
