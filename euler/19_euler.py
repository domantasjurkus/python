'''
* 1 Jan 1900 was a Monday.
* Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4,
  but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(month_num, year):
	return {
	    0: 31, 1: 29 if isYearLeap(year) else 28,
	    2: 31, 3: 30, \
	    4: 31, 5: 30, \
	    6: 31, 7: 31, \
	    8: 30, 9: 31, \
	    10: 30, 11: 31
	}[month_num]

def daysInYear(year):
	return 366 if isYearLeap(year) else 365

SundaysFound = 0

# We need to know on which weekday each year starts
lastWeekDay = 0

for year in xrange(1901, 2001):
	print "----- Year " + str(year) + " -----"
	totalDays = daysInYear(year)
	currentDay = 1
	# Our year has 365 days (the function will catch leap years)
	# now we need to find out which one of those were the 1st of a month

	# every year starts with a '1st of a month' day
	firstDayList = []
	for i in xrange(12):
		firstDayList.append(currentDay)
		daysInOneMonth = daysInMonth(i, year)
		currentDay += daysInOneMonth

	print "First days of month list:", firstDayList

	# now we loop through each week, resetting currentDay
	currentDay = 1

	# weeklyDay represents Mondays, ..., Sundays, only in numeric fashion
	weekDay = lastWeekDay + 1
	if weekDay == 6:
		SundaysFound += 1
	print "First day of the year was", weekDay

	while currentDay < totalDays:
		currentDay += 1
		weekDay = (weekDay+1) % 7
		if currentDay in firstDayList and weekDay == 6:
			print currentDay, "weekday", weekDay
			SundaysFound += 1

	# We are done with the year - save the weekday
	lastWeekDay = weekDay
	print "Sundays so far:", SundaysFound

print SundaysFound