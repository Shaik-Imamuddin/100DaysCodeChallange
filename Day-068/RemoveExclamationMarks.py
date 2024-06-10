#RemoveExclamationMarks

#By using join method
s=input()                   #Time Complexity:O(n)
print(''.join([x for x in s if x != '!']))
print("--------------------------------")

#By using replace method
s=input()
s=s.replace('!', '')            #Time Complexity:O(n)
print(s)
print("--------------------------------")

#By using looping statements
s=input()
s1=''
for i in s:         #Time Complexity:O(n)
    if i!='!': 
        s1+=i
print(s1)
