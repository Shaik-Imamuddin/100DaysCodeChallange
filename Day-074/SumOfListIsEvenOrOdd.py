#SumOfListIsEvenOrOdd

#By using logical operators
n=int(input())
arr=[]
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    arr.append(i)
print(sum(arr) % 2 and 'odd' or 'even')
print("----------------------------")

#By using list indexing
n=int(input())
arr=[]
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    arr.append(i)
print(['even','odd'][sum(arr)%2])
print("----------------------------")

#By using conditional statements
n=int(input())
arr=[]
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    arr.append(i)
print('odd' if sum(arr) & 1 else 'even')
print("----------------------------")

#By using conditional statements alobng with loops
n=int(input())
arr=[]
for i in range(n):      #Time Complexity:O(n)
    i=int(input())
    arr.append(i)
sum=0
for i in arr:
    sum=sum+i
if sum%2==0:
    print("even")
else:
    print("odd")
print("----------------------------")

#By using conditional statements
n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)       #Time Complexity:O(n)
sum = sum(arr)
if sum % 2 == 0:
    print("even")
else:
    print("odd")
