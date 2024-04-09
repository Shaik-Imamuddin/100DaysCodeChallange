#Lucky Number

#Write a program to find if a number is lucky or not.
#If the sum of all digits is 0 or multiple of 9 then the number is lucky.

#1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisible by 9, hence number is lucky.

#print true for lucky numbers and false for others.


#By using looping statements 
n=int(input())
sum=0
l=str(n).split()            #Time-complexity: O(log n)
for i in l:
    sum=sum+int(i)
print(True if sum%9==0 else False)


#Directly By dividing with 9
print("-------------------------------")
n=int(input())
print(n % 9 == 0)               #Time-complexity: O(1)

#By using list comprehension.
print("-------------------------------")
n=int(input())
print(sum([int(i) for i in str(n)]) % 9 == 0)       #Time-complexity: O(log n)
