#Desending Order

#By  type casting into string and using Join method
num=int(input())
strnum = ''.join(sorted(str(num), reverse = True))      #Time Complexity:O(n log n)
print(int(strnum))
print("----------------------------------")
#we can compress the code by Typecasting into integer in the same line
num=int(input())
print(int(''.join(sorted(list(str(num)),reverse=True))))    #Time Complexity:O(n log n)
print("----------------------------------")
#This is also same method as above
num=int(input())
print(int("".join(sorted(str(num), reverse=True))))     #Time Complexity:O(n log n)
print("----------------------------------")
#By using string slicing
num=int(input())
print(int(''.join(sorted(str(num))[::-1])))     #Time Complexity:O(n log n)
print("----------------------------------")
#By typr casting into all methods by using same variable name
num=int(input())
s = str(num)
s = list(s)
s = sorted(s)
s = reversed(s)
s = ''.join(s)
print(int(s))           #Time Complexity:O(n log n)
print("----------------------------------")
#By using List comprehension.
num=int(input())
digits=[int(i) for i in str(num)]       #Time Complexity:O(n log n)
digits.sort(reverse=True)
print(int("".join(map(str,digits))))
