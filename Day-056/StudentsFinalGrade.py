#Students final Grade

#By using logical operators
exam=int(input())
projects = int(input())                         #Time Complexity:O(1)
print(((exam>90 or projects>10) and 100 or 
    exam>75 and projects>=5 and 90 or
    exam>50 and projects>=2 and 75 or 0))


#By using conditional statements
exam=int(input())
projects = int(input())
if exam>90 or projects>10: print(100)
elif exam>75 and projects>=5: print(90)     #Time Complexity:O(1)
elif exam>50 and projects>=2: print(75)
else:print(0)

#We can compress the code By using conditional statements into a single line
exam=int(input())
projects = int(input())     #Time Complexity:O(1)
print(100 if exam > 90 or projects > 10 else 90 if exam > 75 and projects >= 5 else 75 if exam > 50 and projects >=2 else 0)
