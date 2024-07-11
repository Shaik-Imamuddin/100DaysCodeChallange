#Square(n)Sum

import numpy
#By using exponential operator
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())      #Time Complexity: O(n)
    numbers.append(i)
print(numbers)
print(sum(x ** 2 for x in numbers))
#By using list comprhension
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity: O(n)
print(numbers)
print(sum([x * x for x in numbers]))

#By using pow() method along with loop
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity: O(n)
print(numbers)
print(sum(pow(i, 2) for i in numbers))

#By using multiplication operator
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)   #Time Complexity: O(n)
print(numbers)
res = 0
for num in numbers:
    res = res + num*num
print(res)

#By using numpy library
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())          #Time Complexity: O(n)
    numbers.append(i)
print(numbers)
print(sum(numpy.array(numbers) ** 2))
