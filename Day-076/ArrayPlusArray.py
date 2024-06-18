#By using looping statements
n1=int(input("Enter size of arr1:"))
arr1=[]
for i in range(1,n1+1):
    i=int(input(f"Enter element {i}:"))
    arr1.append(i)
n2=int(input("Enter size of arr2:"))
arr2=[]
for i in range(1,n2+1):
    i=int(input(f"Enter element {i}:"))     #Time Complexity:O(n1+n2)
    arr2.append(i)
sum1=0
for i in arr1:
    sum1+=i
for i in arr2:
    sum1+=i
print("The sum of 2 arrays:",sum1)
print("----------------------------")

#By using tuple comprehension
n1=int(input("Enter size of arr1:"))
arr1=[]
for i in range(1,n1+1):
    i=int(input(f"Enter element {i}:"))
    arr1.append(i)
n2=int(input("Enter size of arr2:"))        #Time Complexity:O(n1+n2)
arr2=[]
for i in range(1,n2+1):
    i=int(input(f"Enter element {i}:"))
    arr2.append(i)
print("The sum of 2 arrays:",sum(i for a in [arr1, arr2] for i in a))
print("----------------------------")

#By using sum method along with *args
n1=int(input("Enter size of arr1:"))
arr1=[]
for i in range(1,n1+1):
    i=int(input(f"Enter element {i}:"))     #Time Complexity:O(n1+n2)
    arr1.append(i)
n2=int(input("Enter size of arr2:"))
arr2=[]
for i in range(1,n2+1):
    i=int(input(f"Enter element {i}:"))
    arr2.append(i)
print("The sum of 2 arrays:",sum([*arr1,*arr2]))
print("----------------------------")

#By using sum method along with addition of 2 lists
n1=int(input("Enter size of arr1:"))
arr1=[]
for i in range(1,n1+1):
    i=int(input(f"Enter element {i}:"))
    arr1.append(i)
n2=int(input("Enter size of arr2:"))        #Time Complexity:O(n1+n2)
arr2=[]
for i in range(1,n2+1):
    i=int(input(f"Enter element {i}:"))
    arr2.append(i)
print("The sum of 2 arrays:",sum(arr1+arr2))
print("----------------------------")

#By adding sum of list1 and sum of list2
n1=int(input("Enter size of arr1:"))
arr1=[]
for i in range(1,n1+1):
    i=int(input(f"Enter element {i}:"))     #Time Complexity:O(n1+n2)
    arr1.append(i)
n2=int(input("Enter size of arr2:"))
arr2=[]
for i in range(1,n2+1):
    i=int(input(f"Enter element {i}:"))
    arr2.append(i)
print("The sum of 2 arrays:",sum(arr1)+sum(arr2))
