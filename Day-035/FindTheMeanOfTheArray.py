#FindTheMeanOfTheArray

#By using floor division operator.
n=int(input())
arr=[]
for i in range(n):
    i=int(input())      #Time complexity : O(n)
    arr.append(i)
print(arr)
print(sum(arr)//len(arr))

#By using numpy library
import numpy
n=int(input())
arr=[]
for i in range(n):      #Time complexity : O(n)
    i=int(input())
    arr.append(i)
print(arr)
print(numpy.mean(arr))

#By using Statistics library
import statistics
n=int(input())
arr=[]
for i in range(n):      #Time complexity : O(n)
    i=int(input())
    arr.append(i)
print(arr)
print(statistics.mean(arr))
