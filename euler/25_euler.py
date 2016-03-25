fibs = {}

def fib(n):
    if n < 3:
        return 1
    else:
        if fibs.has_key(n):
            return fibs[n]
        else:
            num = fib(n-1) + fib(n-2)
            fibs[n] = num
            return num

i = 1
while True:
    num = fib(i)

    if len(str(num)) >= 1000:
        print "found it:"
        print i
        break
    i += 1
