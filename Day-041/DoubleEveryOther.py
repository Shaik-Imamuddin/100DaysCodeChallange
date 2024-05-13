#DoubleEveryOther

#By using enumerate function
n=int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)
for i, item in enumerate(lst):
    if i % 2 != 0:
        lst[i] = item*2
print(lst)

#By appending the elements into new list
n=int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)
x = []
for i in range(len(lst)):
    if i % 2 != 0:
        x.append(lst[i] * 2)
    else:
        x.append(lst[i])
print(x)

#By using list comprehension
n=int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)
print([x * 2 if i % 2 == 1 else x for i, x in enumerate(lst)])
