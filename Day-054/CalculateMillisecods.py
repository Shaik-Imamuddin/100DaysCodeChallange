#CaluculateMilliseconds

#By calculating the each and every input with max input values
h=int(input())
m=int(input())      #Time Complexity:O(1)
s=int(input())
print(((h*3600)*1000)+((m*60)*1000)+(s*1000))

#By adding all the values and doing Multiplication with 1000
h=int(input())
m=int(input())      #Time Complexity:O(1)
s=int(input())
print((3600*h + 60*m + s) * 1000)
