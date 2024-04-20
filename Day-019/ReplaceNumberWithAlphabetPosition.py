#Description:
#given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#"a" = 1, "b" = 2, etc.



#By using lists we can get the index
text=input()
answer = ""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z']
for char in text.lower():       #Time Complexity:O(n)
    if char in alphabet:
        answer += (str(alphabet.index(char) + 1) + " ")
print(answer[:-1])

#By using join method
text=input()            #Time Complexity:O(n)
print(' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()))


#By using ord value
text=input()
s=''
for i in text.lower():          #Time Complexity:O(n)
    if i>='a' and i<='z':
        r=ord(i)-96
        s=s+str(r)+" "
print(s.strip())
