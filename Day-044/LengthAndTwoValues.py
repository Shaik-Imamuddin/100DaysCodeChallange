#By using for loop along with step value
n=int(input())
first_value=input()
second_value=input()
arr = [first_value]*n
for i in range(1, n, 2):        #Time Complexity:O(n)
    arr[i] = second_value
print(arr)


#By using for loop along with conditions
n=int(input())
first_value=input()
second_value=input()
myList = [first_value]*n
for i in range(n):
    if(i%2!=0):                     #Time Complexity:O(n)
        myList[i] = second_value
print(myList)

#By using list comprehension
n=int(input())
first_value=input()             #Time Complexity:O(n)
second_value=input()
print([first_value if i % 2 == 0 else second_value for i in range(n)])

#By using nested list comprehension
n=int(input())
first_value=input()         #Time Complexity:O(n)
second_value=input()
print([[first_value, second_value][i % 2] for i in range(n)])
