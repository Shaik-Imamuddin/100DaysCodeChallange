#NoZerosForHeros

#By using loops and conditions
n=int(input())
if n==0:
    print(n)
while n%10==0:      #Time Complexity:O(n)
    n=n//10
print(n)

#we can compress the code by using two conditions in a loop.
n=int(input())
while n and n % 10 == 0:        #Time Complexity:O(n)
    n //= 10
print(n)

#Only By using conditional statements.
n=int(input())
if n==0:
    print(0)
else:
    s=str(n).strip('0')     #Time Complexity:O(n)
    print(int(s))

#By using rstrip() method.
n=int(input())
print(int(str(n).rstrip("0")) if n else n)      #Time Complexity:O(n)

#By using strip method.
n=int(input())
print(int(str(n).strip("0")) if n else n)       #Time Complexity:O(n)
