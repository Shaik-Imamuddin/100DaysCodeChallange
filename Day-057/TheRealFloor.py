#By using relational Operators
n=int(input())
print(n - (n > 0) - (n > 13))       #Time Complexity:O(1)

print("----------------------------------------")
#By using conditional statements
n=int(input())
if n>=13:
    print(n-2)
elif(n<=0):
    print(n)
else:print(n-1)     #Time Complexity:O(1)

print("----------------------------------------")
#we can compress the above code within one line
n=int(input())
print(n if n < 1 else n - 1 if n < 13 else n - 2)       #Time Complexity:O(1)

