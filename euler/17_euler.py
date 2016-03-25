# just maths
from math import *

# for numbers [1, 20]
def getLetterCount20(num):
    count = 0
    
    if num==1:       # "one"
        count += 3
    elif num==2:     # "two"
        count += 3
    elif num==3:     # "three"
        count += 5
    elif num==4:     # "four"
        count += 4
    elif num==5:     # "five"
        count += 4
    elif num==6:     # "six"
        count += 3
    elif num==7:     # "seven"
        count += 5
    elif num==8:     # "eight"
        count += 5
    elif num==9:     # "nine"
        count += 4
    elif num==10:    # "ten"
        count += 3

    elif num==11:   # "eleven"
        count += 6
    elif num==12:   # "twelve"
        count += 6
    elif num==13:   # "thirteen"
        count += 8
    elif num==14:   # "fourteen"
        count += 8
    elif num==15:   # "fifteen"
        count += 7
    elif num==16:   # "sixteen"
        count += 7
    elif num==17:   # "seventeen"
        count += 9
    elif num==18:   # "eighteen"
        count += 8
    elif num==19:   # "nineteen"
        count += 8
    elif num==20:   # "twenty"
        count += 6
    return count
# for numbers [1, 99]
def getLetterCount99(num):
    count = 0

    if num <= 20:
    	count = getLetterCount20(num)
    elif num < 30:  # twenty ...
        count += 6
        count += getLetterCount20(num%10)
    elif num < 40:  # thirty ...
        count += 6
        count += getLetterCount20(num%10)
    elif num < 50:  # forty ...
        count += 5
        count += getLetterCount20(num%10)
    elif num < 60:  # fifty ...
        count += 5
        count += getLetterCount20(num%10)
    elif num < 70:  # sixty ...
        count += 5
        count += getLetterCount20(num%10)
    elif num < 80:  # seventy ...
        count += 7
        count += getLetterCount20(num%10)
    elif num < 90:  # eighty ...
        count += 6
        count += getLetterCount20(num%10)
    elif num < 100: # ninety ...
        count += 6
        count += getLetterCount20(num%10)

    return count

def count(num):
    count = 0

    # 1000
    if num == 1000:     # "one thousand"
        count = 11

    # [100, 999]
    elif num >= 100:

        # 100, 200, 300, 400, ...
        if num % 100 == 0:	
        	count += getLetterCount20(num/100)	# "one/two/three/..."
        	count += 7 							# "hundred"

        # 101, 102, 103, ...
        else:	
        	count += getLetterCount20(num/100)	# "one/two/three/..."
        	count += 10 						# "hundred and"
        	count += getLetterCount99(num%100)	# "one/two/three/..."

    # (21, 99)
    elif num > 20:
        count = getLetterCount99(num)

    # (1, 20)
    elif num > 0: 
        count = getLetterCount20(num)


    return count

letter_sum = 0
for num in range(1, 1001):
    letter_sum += count(num)

print letter_sum
