#write a program that will take 2 integer inputs x and n.
#return an array of the first n multiples of x.

#using loop
x,n=int(input("Enter x value:")),int(input("Enter n value:"))
l=[]
for i in range(n):      #Time Complexity:O(n)
    l.append(x)
    x=x+l[0]
print(l)
print("-------------------------")
#using list comprehension
x,n=int(input("Enter x value:")),int(input("Enter n value:"))
l=[i * x for i in range(1, n + 1)]      #Time Complexity:O(n)
print(l)
print("-------------------------")
#using range function
x,n=int(input("Enter x value:")),int(input("Enter n value:"))
l=list(range(x, n * x + 1, x))      #Time Complexity:O(n)
print(l)
print("-------------------------")
