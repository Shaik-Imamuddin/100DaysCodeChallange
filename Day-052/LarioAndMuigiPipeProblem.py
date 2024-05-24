#LarioAndMuigiPipeProblem

#By using for loop
nums=[]
n=int(input())
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    nums.append(i)
print(nums)
l = []
for i in range(nums[0], nums[-1] + 1):
    l.append(i)
print(l)

#By using list comprehension with min and max methods
nums=[]
n=int(input())
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    nums.append(i)
print(nums)
print([i for i in range(min(nums),max(nums)+1)])

#By using list method
nums=[]
n=int(input())
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    nums.append(i)
print(nums)
print(list(range(nums[0],nums[-1]+1)))

#By using list comprehension with indexing
nums=[]
n=int(input())
for i in range(n):
    i=int(input())
    nums.append(i)      #Time Complexity:O(n)
print(nums)
print([i for i in range(nums[0],nums[-1]+1)])
