#StringReverse

#By using string Slicing
string=input()
print(string[::-1])     #Time Complexity:O(n)

#By using reverse and join methods
string=input()
temp = list(string)
temp.reverse()
print(''.join(temp))        #Time Complexity:O(n)

#By using join method along with string comprehension
string=input()
print(''.join(i for i in reversed(string)))     #Time Complexity:O(n)

#By using string concatination
string=input()
s1=''
for x in string:        #Time Complexity:O(n^2)
    s1= x+s1
print(s1)

#By using list comprehension along with join method and string Slicing
string=input()
str = [str for str in string]   #Time Complexity:O(n)
print(''.join(str[::-1]))


#By using reversed method
string=input()
print("".join(reversed(string)))    #Time Complexity:O(n)
