#CountOfPositiveSumOfNegative


#By using list comprehension
n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)
print(arr)
output = []
if arr:
    output.append(sum([1 for x in arr if x > 0]))       #Time Complexity:O(n)
    output.append(sum([x for x in arr if x < 0]))
print(output)

#By using sum method and loops
n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)
print(arr)          #Time Complexity:O(n)
if not arr:
    print(arr)
print([sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)])


#By Intializing the variables as 0
n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)       #Time Complexity:O(n)
print(arr)
sum,count = 0,0
if (len(arr) == 0):
    print([])
for i in arr:
    if i > 0:
        count += 1
    else:
        sum = sum + i    
print([count,sum])
