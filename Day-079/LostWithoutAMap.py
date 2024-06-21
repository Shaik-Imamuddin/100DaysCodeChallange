#LostWithoutAMap

#By using append() method
n=int(input())
lst=[]
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    lst.append(i)
print(lst)
l=[]
for i in lst:
    l.append(i*2)
print(l)

#By using list comprehension
n=int(input())
lst=[int(input()) for i in range(n)]        #Time Complexity:O(n)
print(lst)
print([i*2 for i in lst])
