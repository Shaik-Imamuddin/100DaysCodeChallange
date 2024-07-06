#By using conditional statements
numbers=[]
n=int(input())
for i in range(n):
    i=int(input())
    numbers.append(i)
print(numbers)              #Time Complexity:O(n)
if len(numbers)==0:
    print(0)
print(sum(numbers)/len(numbers))

#We can compress the code by using conditional statements
numbers=[]
n=int(input())
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity:O(n)
print(numbers)
print(sum(numbers)/len(numbers) if numbers else 0)

#Method-2 of We can compress the code by using conditional statements
numbers=[]
n=int(input())
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity:O(n)
print(numbers)
print(0 if len(numbers)==0 else sum(numbers)/len(numbers))
