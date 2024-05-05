#FineMinAndMaxValueOfAList

#By using sorted Method
n=int(input())
l=[]
for i in range(n):
    i=int(input())          #Time Complexity: O(nlogn)
    l.append(i)
print(sorted(l)[0],sorted(l)[-1])


#By using min and max methods
n=int(input())
l=[]
for i in range(n):
    i=int(input())
    l.append(i)             #Time Complexity: O(n)
print(min(l),max(l))


#By using loops we can search min and max element
n=int(input())
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
low=l[0]
high = l[0]
for i in l[1:]:         #Time Complexity: O(n)
    if i < low:
        low = i
for i in l[1:]:
    if i > high:
        high = i
print(low,high)
