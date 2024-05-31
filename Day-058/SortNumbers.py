#By using If conditions
nums=[]
n=int(input())
for i in range(n):
    i=int(input())
    nums.append(i)
print(nums)
if not nums:
    print([])               #Time Complexity:O(n log n)
else:
    print(sorted(nums))
print("-----------------------------------")
#we can compress the above code By using condition in print statement
nums=[]
n=int(input())
for i in range(n):
    i=int(input())
    nums.append(i)      #Time Complexity:O(n log n)
print(nums)
print(sorted(nums) if nums else[])

print("-----------------------------------")
#By using Logical operators
nums=[]
n=int(input())
for i in range(n):
    i=int(input())
    nums.append(i)      #Time Complexity:O(n log n)
print(nums)
print(sorted(nums or []))

print("-----------------------------------")
#By using the new list along with append ,min and remove functions
nums=[]
n=int(input())
for i in range(n):
    i=int(input())
    nums.append(i)
print(nums)     #Time Complexity:O(n^2)
l=[]
if nums==None or nums==[]:
    print([])
else:
    for i in range(len(nums)):
        m=min(nums)
        l.append(m)
        nums.remove(m)
    print(l)
