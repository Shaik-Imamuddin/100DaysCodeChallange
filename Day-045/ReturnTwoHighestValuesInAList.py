#ReturnTwoHighestInAList

#By using set along with Slicing
n=int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)       #Time Complexity:O(n log n)
print(lst)
print(sorted(set(lst))[-2:][::-1])

#By using set along with reverse attribute
n=int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)                      #Time Complexity:O(n log n)
l=sorted(set(lst), reverse=True)
print(l[:2])

#We can compress the above code into a single line
n=int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)                  #Time Complexity:O(n log n)
print(sorted(set(lst), reverse=True)[:2])
