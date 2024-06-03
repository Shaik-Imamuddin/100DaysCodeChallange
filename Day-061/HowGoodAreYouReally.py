#HowGoodAreYouReally

#By using Comparision Operators along with conditional statements
class_points=[]
n=int(input())
for i in range(n):
    i=int(input())
    class_points.append(i)      #Time Complexity:O(n)
your_points=int(input())
if sum(class_points)//len(class_points)>=your_points:
    print(False)
else:
    print(True)

print("-------------------------------------")
#We can compress the above code By using conditions in a print statement
class_points=[]
n=int(input())
for i in range(n):
    i=int(input())
    class_points.append(i)      #Time Complexity:O(n)
your_points=int(input())
print(True if sum(class_points)//len(class_points)<=your_points else False)

print("-------------------------------------")
#Without using conditional statements
class_points=[]
n=int(input())
for i in range(n):
    i=int(input())
    class_points.append(i)      #Time Complexity:O(n)
your_points=int(input())
print(your_points > sum(class_points) / len(class_points))


