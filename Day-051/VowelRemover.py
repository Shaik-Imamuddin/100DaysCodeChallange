#VowelRemover

#By using replace method in a loop
s=input()
for i in ["a","e","i","o","u"]:
    s=s.replace(i,"")       #Time Complexity:O(n)
print(s)

#By using replace method inside a loop and condition
s=input()
for i in s:
    if i in "aeiou":
        s=s.replace(i,"")       #Time Complexity:O(n^2)
print(s)

#By using join method
s=input()
print("".join(i for i in s if i not in "aeiou"))    #Time Complexity:O(n)

#By using string Concatenation
s=input()
s1=''
for i in s:
    if i not in "aeiou":        #Time Complexity:O(n^2)
        s1+=i
print(s1)
