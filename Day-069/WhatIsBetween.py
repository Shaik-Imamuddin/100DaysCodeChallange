#WhatIsBetween

#By using for loop
a=int(input())
b=int(input())      #Time Complexity:O(n)
lst=[]
for i in range(a,b+1):
    lst.append(i)
print(lst)

print("-----------------------------------")
#By using list() and range() methods
a=int(input())
b=int(input())
res=list(range(a,b+1))      #Time Complexity:O(n)
print(res)
print("-----------------------------------")

#By using list comprehension
a=int(input())
b=int(input())
print([i for i in range(a,b+1)])        #Time Complexity:O(n)
