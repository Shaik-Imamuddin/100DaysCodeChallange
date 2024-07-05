#YouOnlyNeedOne

#By using in operator
seq=int(input())
l=[]
for i in range(seq):
    i=input()
    l.append(i)     #Time Complexity:O(n)
elem=input()
print(elem in l)

#By using Conditional statements
seq=int(input())
l=[]
for i in range(seq):
    i=input()           #Time Complexity:O(n)
    l.append(i)
elem=input()
print(True if elem in l else False)
