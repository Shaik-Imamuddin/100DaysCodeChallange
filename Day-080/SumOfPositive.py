#SumOfPositive

#By using looping statements
n=int(input())
arr=[]
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    arr.append(i)
result=0
for i in arr:
    if i>0:
        result+=i
print(result)

#By using List comprehension
num=int(input())
arr=[]
for i in range(num):
    i=int(input())      #Time Complexity:O(n)
    arr.append(i)
print(sum([x for x in arr if x > 0]))

#By using Tuple comprehension
num=int(input())
arr=[]
for i in range(num):
    i=int(input())      #Time Complexity:O(n)
    arr.append(i)
print(sum(x for x in arr if x > 0))
