#replace all vowels with an exclamation mark in the sentence 

#By using replace method with strings
s=input()
vowels ='aeiouAEIOU'
for i in vowels:
    s=s.replace(i, '!')         #Time Complexity:O(n^2)
print(s)

print("--------------------------------------")
#By using replace method with lists
s=input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in s:
    if i in vowels:
        s = s.replace(i,'!')            #Time Complexity:O(n^2)
print(s)
print("--------------------------------------")
#By using sub() method
import re
s=input()
print(re.sub('[aeiouAEIOU]', '!', s))           #Time Complexity:O(n)
print("--------------------------------------")
#By using translate and maketrans method
s=input()
print(s.translate(s.maketrans('aeiouAEIOU', '!!!!!!!!!!')))   #Time Complexity:O(n)

#By using join Method
print("--------------------------------------")
s=input()
print(''.join('!' if i in 'aeiouAEIOU' else i for i in s))      #Time Complexity:O(n)

print("--------------------------------------")
#By using loops with string concatination
s=input()
r=""
for i in s:
    if i in "aeiouAEIOU":           #Time Complexity:O(n)
        r+="!"
    else:
        r+=i
print(r)
