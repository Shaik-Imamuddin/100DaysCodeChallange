#sum of n numbers
n=int(input("Enter n value:"))
sum=0
for i in range(n+1):
    sum+=i          #time complexity: O(n)
print(sum)


n=int(input("Enter n value:"))
sum=0
for i in range(n):
    for i in range(i):
        sum+=i          #time complexity: O(n^2)
print(sum)



n=int(input("Enter n value:"))
sum= n*(n+1)//2     #time complexity: O(1)
print(sum)


#BestCase = O(1) - Constant Time
#BestCase = O(n) - Linear Time
#Average Case = O(n^2) - Quadratic Time
