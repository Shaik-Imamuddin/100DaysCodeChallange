#PowersOf2

#By using Exponential operator along with append
n=int(input())
l = []
for i in range(0, n + 1):       #Time Complexity: O(n)
    l.append(2 ** i)    
print(l)


#By using List comprehension
n=int(input())
print([2**i for i in range(n+1)])       #Time Complexity: O(n)
