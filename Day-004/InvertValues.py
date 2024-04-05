#INVERT VALUES

#using Loops
n=int(input("Enter List Length:"))
lst=[]
for i in range(n):
    i=int(input("Enter List values:"))
    lst.append(i)
lst1=[]
for num in lst:
    lst1.append(num*-1)     #Time Complexity:O(n)
print(lst)
print(lst1)


#Using List comprehension
n=int(input("Enter List Length:"))
lst = [int(input("Enter List Elements:")) for x in range(n)]
print(lst)
lst1=[-i for i in lst]      #Time Complexity:O(n)
print(lst1)
