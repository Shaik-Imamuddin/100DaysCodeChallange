#CasingStrings

#By using String Concatenation
string=input()
s=''
l=string.split()
for i in l:
    u=i.capitalize()        #Time Complexity:O(n^2)
    s+=u+" "
print(s[:-1])

#By using join method along with capitalize,for loop and split method.
string=input()      #Time Complexity:O(n)
print(' '.join(word.capitalize() for word in string.split()))

#By using join method along with map ,capitalize and split method.
string=input()      #Time Complexity:O(n)
print(' '.join(map(str.capitalize, string.split())))

#By using capwords methos which is available in String package.
import string
s=input()       #Time Complexity:O(n)
print(string.capwords(s))
