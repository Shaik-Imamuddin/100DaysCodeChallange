#Multiply the number

#By using math module

import math
n=int(input())
count = int(math.log10(abs(n)) + 1) if n else 1  #Time Complexity:O(log(n))
print(n * 5**count)

print("-----------------------------")
#By type casting into string
n=int(input())
s = str(n)
s = s.replace('-','')           #Time Complexity:O(log(n))
a = len(s)
print(n * 5**a)
print("-----------------------------")
#We can compress the above code

#The abs() will return The absolute value of a number is its distance from zero on the number line
n=int(input())
p=len(str(abs(n)))          #Time Complexity:O(log(n))
print(n*(5**p))
print("-----------------------------")
