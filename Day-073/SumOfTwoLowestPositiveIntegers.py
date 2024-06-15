#SumOfTwoLowestPositiveIntegers

#By using sorted method along with indexing
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity:O(n log n)
print(numbers)
print(sorted(numbers)[0] + sorted(numbers)[1])

#By using sort() method along with indexing
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity:O(n log n)
print(numbers)
numbers.sort()
print(numbers[0]+numbers[1])

#By using sum() and sorted() methods along with slicing
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity:O(n log n)
print(numbers)
print(sum(sorted(numbers)[:2]))

#By using min() and max() functions
n=int(input())
numbers=[]
for i in range(n):
    i=int(input())
    numbers.append(i)       #Time Complexity:O(n)
print(numbers)
m=min(numbers)
numbers.remove(m)
l=numbers
n=min(l)
print(m+n)
