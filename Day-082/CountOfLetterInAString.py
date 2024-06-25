#CountOfLetterInAString

#By using comparision operator
strng=input()
letter=input()
count=0
for i in strng:     #Time Complexity:O(n)
    if i==letter: 
        count+=1
print(count)

#By using count() method 
strng=input()
letter=input()              #Time Complexity:O(n)
print(strng.count(letter))

#By using len() and list comprehension
strng=input()                   
letter=input()          #Time Complexity:O(n)
print(len([x for x in strng if x == letter]))

#By using findall() method in re package
import re
strng=input()       #Time Complexity:O(n)
letter=input()
print(len(re.findall(f"{letter}", strng)))

#By using sum method along with tuple comprehension
strng=input()   
letter=input()      #Time Complexity:O(n)
print(sum(1 for i in strng if i == letter))
