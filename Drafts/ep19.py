#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

week = ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun']
month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
day30 = ['apr', 'jun', 'sept', 'nov']
day31 = ['jan', 'mar', 'apr', 'may', 'jul', 'aug', 'oct', 'dec']
feb = 28

e = 'feb'
fromday = 0
frommonth = 0
fromyear = 1901

def daymonth(e):
    d = 0
    if e in day30:
      d = 30
    if e in day31:
      d = 31
    else:
      d = feb
    return d

def letsgo():
    year = 365
    #decision to postpone this problem was made here
    for i in range(0,year+1):
      fromday += 1



f = daymonth(e)
print(f)


#Process: reading the problem description is a promlem in itself. Would have stabbed caesar myself tbh.
#Disgusting.
