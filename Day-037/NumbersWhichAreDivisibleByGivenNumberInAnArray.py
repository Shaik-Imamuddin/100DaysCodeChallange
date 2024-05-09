#NumbersWhichAreDivisibleByGivenNumberInAnArray

#By using looping statements 
n=int(input("Enter Array Length:"))
l = []
for i in range(n):
    i=int(input())      #Time Complexity:O(n)
    l.append(i)
print(l)
divisor=int(input("Enter the Divisor:"))
factors=[]
for i in l:
    if i%divisor==0:
        factors.append(i)
print(factors)

#By using liist comprehension
n=int(input("Enter Array Length:"))
l = []
for i in range(n):
    i=int(input())          #Time Complexity:O(n)
    l.append(i)
print(l)
divisor=int(input("Enter the Divisor:"))
print([i for i in l if i%divisor==0])
