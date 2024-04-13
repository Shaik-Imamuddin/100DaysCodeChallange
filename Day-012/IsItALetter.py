#Write a program, which tells us if a given character is a letter or not.

#By using isalpha() Method
s=input()
print(s.isalpha())      #Time Complexity :O(1).

print(True if s.isalpha() else False)


#by using in operator
s=input()
if s in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKKLZXCVBNM':
    print(True)         #Time Complexity :O(1).
else:
    print(False)

#by Using isupper() and islower() methods
s=input()
for i in s:
    if i.isupper() or i.islower():      #Time Complexity :O(1).
        print(True)
    else:
        print(False)


