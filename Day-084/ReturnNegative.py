#Return Negative

#By using if elif else ststements
number=int(input())
if 0:print(0)
elif number<0:print(number)     #Time Complexity:O(1)
else: print(-number)


#Only By using if else statements
number=int(input())
if number >= 0:
    print((0 - number))     #Time Complexity:O(1)
else:
    print(number)


#By using abs function
number=int(input())
print(-abs(number))     #Time Complexity:O(1)
