
#The cockroach is one of the fastest insects.
#write a program which takes its speed in km per hour
#and returns it in cm per second, rounded down to the integer (= floored).

#By assgining the values and converting them cm per second
s=float(input())
cm_per_km = 100000
sec_per_hour = 3600
print(int(s * cm_per_km / sec_per_hour))    #Time Complexity: O(1)

#Directly by doing the floor division 
s=float(input())
print(int(s * 100000) // (60 * 60))     #Time Complexity: O(1)

#by multiplying with the value 27.7778 we can get the output
s=float(input())
print(int(s * 27.7778))     #Time Complexity: O(1)

#By Dividing with the value which we can get (100000) // (60 * 60) from this Expression
s=float(input())
print(int(s // 0.036))      #Time Complexity: O(1)


#by using floor() method 
import math
s=float(input())
res=(s*100000)/3600
print(math.floor(res))          #Time Complexity: O(1)
