#Transportation on Vacation

#By using conditional Statements
d=int(input())
if d>=7:
    print((40*d)-50)        #Time Complexity:O(1)
elif d>=3:
    print((40*d)-20)
else:
    print(40*d)


#By multiplying the input with all maxium values
d=int(input())
print(d * 40 - (d > 2) * 20 - (d > 6) * 30)     #Time Complexity:O(1)
