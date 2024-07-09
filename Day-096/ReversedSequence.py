#ReversedSequence

#By using List and range methods
n=int(input())
print(list(range(n, 0, -1)))    #Time Complexity:O(n)

#By using list Comprehension
n=int(input())
print([x for x in range(n,0,-1)])       #Time Complexity:O(n)

#By using loop and append method
n=int(input())
output = []
for i in range(n):
    output.append(n)    #Time Complexity:O(n)
    n -= 1
print(output)

#using list comprehension along with indexing
n=int(input())
print([x for x in range(1,n+1)][::-1])      #Time Complexity:O(n)

#By using reverse method
n=int(input())
l = [x for x in range(1,n+1)]       #Time Complexity:O(n)
l.reverse()
print(l)
