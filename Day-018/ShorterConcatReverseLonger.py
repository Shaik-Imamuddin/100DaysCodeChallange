#Description:

#Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.
#In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

#By using slicing and conditions
a=input()
b=input()
if len(a) >= len(b):            
    print(b + a[::-1] + b)      #Time Complexity:O(n)
else:
    print(a + b[::-1] + a)

print("-------------------------------------")
#we can compress the above logic into sigle line
a=input()
b=input()
print(a+b[::-1]+a if len(a)<len(b) else b+a[::-1]+b)        #Time Complexity:O(n)
print("-------------------------------------")
#By using sorted along with key Vlaue
a=input()
b=input()
short,long=sorted((b,a), key=len)
print(short + long[::-1] + short)       #Time Complexity:O(n)
print("-------------------------------------")
#By using join and reversed method
a=input()
b=input()
if len(a) >= len(b):
    a,b = b,a
    print(a+"".join(reversed(b))+a)     #Time Complexity:O(n)
print("-------------------------------------")
#by using format string along with conditions
a=input()
b=input()
if len(a) >= len(b):
      a,b = b,a
      print('{0}{1}{0}'.format(a, b[::-1]))     #Time Complexity:O(n)
