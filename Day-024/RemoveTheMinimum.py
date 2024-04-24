#RemoveTheMinimum

#By using slicing fo list
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())              #Time Complexity:O(n)
    numbers.append(i)           
print(numbers[0:numbers.index(min(numbers))]+numbers[numbers.index(min(numbers))+1:] if numbers else numbers)

Print("----------------------------------")

#By using the remove function along with min function
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)
if not numbers:
    print(numbers)
else:
    new = numbers[:]
    new.remove(min(numbers))            #Time Complexity:O(n^2)
    print(new)
#Is is same as above we can compress without using else condition
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)
l = numbers[:]
if l:
    l.remove(min(l))            #Time Complexity:O(n^2)
    print(l)

#By using only remove function
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)
if len(numbers)>=1:
    s=min(numbers)
    l=numbers[:]            #Time Complexity:O(n^2)
    l.remove(s)
    print(l)
    else: print([])

#Note:
#l = numbers[:] By using this instuction it will store the values of numbers list to l list.
