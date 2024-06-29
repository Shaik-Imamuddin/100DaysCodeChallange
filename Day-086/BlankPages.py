#BlankPages

#By using conditional statements
m=int(input())
n=int(input())
if n<0 or m<0: print(0)     #Time Complexity:O(1)
else:print(n*m)

#we can compress the code By using conditional statements
m=int(input())
n=int(input())
print(n * m if n > 0 and m > 0 else 0)      #Time Complexity:O(1)

#By using conditional statements along with min() function
m=int(input())
n=int(input())
print(n * m if min((n, m)) > 0 else 0)      #Time Complexity:O(1)
