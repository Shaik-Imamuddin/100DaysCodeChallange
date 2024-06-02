#ConvertArrayOfStringsToArrayOfNumbers

#By using eavl() method
n=int(input())
arr=[]
for i in range(n):
    i=input()
    arr.append(i)   #Time Complexity:O(n)
print(arr)
print([eval(x) for x in arr])

print("------------------------------------")
#By using list() and map() method
n=int(input())
arr=[]
for i in range(n):
    i=input()
    arr.append(i)       #Time Complexity:O(n)
print(arr)
print(list(map(int,arr)))
print("------------------------------------")
#By using Type casting in same list
n=int(input())
arr=[]
for i in range(n):
    i=input()
    arr.append(i)       #Time Complexity:O(n)
print(arr)
print([int(i) for i in arr])
print("------------------------------------")
#By using Type casting using another list
n=int(input())
arr=[]
for i in range(n):
    i=input()
    arr.append(i)       #Time Complexity:O(n)
print(arr)
l=[]
for i in arr:
    s=int(i)
    l.append(s)
print(l)
