#By using conditional statements
lst=[]
n=int(input())
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)
min, max = lst[0], lst[0]       #Time Complexity:O(n)
for i in lst:
    if i > max:
        max = i
    elif i < min:
            min = i
print([min, max])
print("---------------------------------------")
#By using list indexing
lst=[]
n=int(input())
for i in range(n):
    i=int(input())
    lst.append(i)       #Time Complexity:O(n log n)
print(lst)
lst.sort()
print([lst[0],lst[-1]])
print("---------------------------------------")
#By using min() and max() functions
lst=[]
n=int(input())
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    lst.append(i)
print(lst)
print((min(lst),max(lst)))
