#write a program that takes positive integer to calculate sum of its digits.

#using tuple comprehension
num=int(input())
print(sum(int(i) for i in str(num)))    #Time Complexity:O(n)

#using map function
num=int(input())
print(sum(map(int, str(num))))      #Time Complexity:O(n)

#using for loop
num=int(input())
sum = 0
digits = list(str(num))
for x in digits:            #Time Complexity:O(n)
    sum +=int(x)
print(sum)


