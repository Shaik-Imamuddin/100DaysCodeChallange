#SumWithoutHighestAndLowestNumber


#By using sum and sorted method

n=int(input())
l=[]
for i in range(n):
    i=int(input())          #Time Complexity: O(n log n)
    l.append(i)
print(sum(sorted(l)[1:-1]) if l else 0)


#By using sum ,max and min methods

n=int(input())
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
if l == None or len(l) < 3:
    print(0)
print(sum(l) - max(l) - min(l))     #Time Complexity: O(n)


#By using list comprehension along with pop and index method

n=int(input())
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
print(sorted(l))
if l==None or len(l)==1 or len(l)==0:       #Time Complexity: O(n^2)
        print(0)
else:
    m=l.index(max(l))
    l.pop(m)
    n=l.index(min(l))
    l.pop(n)
    print(sum([i for i in l]))
