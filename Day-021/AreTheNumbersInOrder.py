#AreTheNumbersInOrder

#By using sorted method we can compare the numbers are in sorted order or not
n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)
if sorted(arr) == arr:      #Time complexity:O(n log n)
    print(True)
else:
    print(False)
print("-----------------------------------------")

#we can compress the code only by using the condition
n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)
print(arr == sorted(arr))           #Time complexity:O(n log n)
print("-----------------------------------------")
#by using for loop we compare with each and every element
arr = list(map(int, input("Enter numbers separated By space: ").split()))
for i in range(len(arr) - 1):       #Time complexity:O(n)
    if arr[i] > arr[i + 1]:
        print(False)
        break
else:
    print(True)

#Note: we will choose the linear time O(n)
