#QuarterOfTheYear

#By using conditional statements:
month=int(input())
if month>=1 and month <=3: print(1)
elif month>3 and month <=6: print(2)
elif month>6 and month <=9: print(3)        #Time Complexity: O(1)
else: print(4)

#By using conditional statements along with range function
month=int(input())
if month in range(1, 4):
    print(1)
elif month in range(4, 7):
    print(2)
elif month in range(7, 10):
    print(3)
elif month in range(10, 13):        #Time Complexity: O(1)
    print(4)

#We can compress the conditional statements code into one singlr print statement
month=int(input())
print(1 if month<=3 else 2 if month<=6 else 3 if month<=9 else 4)

#By using Dictionaries

month=int(input())
quarter = {1: 1, 2: 1, 3: 1, 
            4: 2, 5: 2, 6: 2,
            7: 3, 8: 3, 9: 3,
            10: 4, 11: 4, 12: 4}        #Time Complexity: O(1)
print(quarter[month])
