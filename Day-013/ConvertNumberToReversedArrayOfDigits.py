#By using reverse() method along with list comprehension.
n=int(input())
mylist = [int(i) for i in str(n)]       #Time Complexity:O(log n)
mylist.reverse()
ptint(mylist)

#By using reversed() method along with list comprehension.
n=int(input())
print([int(x) for x in reversed(str(n))])       #Time Complexity:O(log n)

#By using slicing along with list comprehension.
n=int(input())
print([int(x) for x in str(n)[::-1]])       #Time Complexity:O(log n)

#By using while loop along with append() method.
n=int(input())
l=[]
if(n==0):
    l.append(0)
while(n!=0):            #Time Complexity:O(log n)
    rem=n%10
    l.append(rem)
    n=n//10
print(l)
