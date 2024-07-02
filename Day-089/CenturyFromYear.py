#By using conditional statements
year=int(input())
k=year%10
p=year%100
l=p//10
m=year//100
if(k>0 or l>0):print(m+1)       #Time Complexity:O(1)
else:print(m)

#Another method of using conditional statements
year=int(input())
k=year%100
p=year//100
if(k>0):print(p+1)      #Time Complexity:O(1)
else:print(p)

#By using floor division
year=int(input())
print((year+99)//100)       #Time Complexity:O(1)

