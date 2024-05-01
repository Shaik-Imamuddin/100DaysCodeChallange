#DaysInTheYear

#By using conditional statements
year=int(input())
if year % 100 == 0:
    if year % 400 == 0:                 #Time Complexity: O(1)
        print("%s has 366 days" % year)
    else:
        print("%s has 365 days" % year)
else:
    print("%s has 366 days" % year) if year % 4 == 0 else print("%s has 365 days" % year)

print("-----------------------")

#we can compress code by using the compound condition
year=int(input())
days=365
if (year%4==0 and year%100!=0) or year%400==0:      #Time Complexity: O(1)
    days+=1
print("%d has %d days" % (year, days))


print("-----------------------")
#By using calender module
import calendar
year=int(input())
if calendar.isleap(year):                   #Time Complexity: O(1)
    print('{0} has 366 days'.format(year))
else:
    print('{0} has 365 days'.format(year))


