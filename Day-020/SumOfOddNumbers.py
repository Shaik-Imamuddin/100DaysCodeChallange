#SumOfOddNumbers
#Description
'''
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

'''
#By using For loop
n=int(input())
x = []
for i in range(1,n*n+n,2):      #Time complexity:O(n)
    x.append(i)
print(sum(x[-n:]))
print("--------------------------------------")
#By using range along with sum function.
n=int(input())
print(sum(range(n*(n-1)+1, n*(n+1), 2)))    #Time complexity:O(1)

print("--------------------------------------")
#By using Power function
n=int(input())
print(pow(n,3))         #Time complexity:O(1)
print("--------------------------------------")
#By multiplying n for 3 times
n=int(input())
print(n*n*n)            #Time complexity:O(1)
print("--------------------------------------")
#By using exponential operator
n=int(input())
print(n**3)     #Time complexity:O(1)
print("--------------------------------------")
#By using the below expression
n=int(input())
print(n**2+(n-1)*n**2)      #Time complexity:O(1)

#Note: We choose the Time Complexity:O(1)
