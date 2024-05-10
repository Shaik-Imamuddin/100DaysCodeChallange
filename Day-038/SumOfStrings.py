#sum the strings

#By Type casting
a=input()
b=input()
print(str(int(a or 0) + int(b or 0)))   #Time complexity:O(n)

a=input()
b=input()
print(str(int('0' + a) + int('0' + b))) #Time complexity:O(n)


#By using conditions along with Type casting
a=input()
b=input()
if a == '': a = '0'
if b == '': b = '0'
print(str(int(a) + int(b))) #Time complexity:O(n)


a=input()
b=input()
print('%d' % (int(a if a else 0) + int(b if b else 0))) #Time complexity:O(n)
