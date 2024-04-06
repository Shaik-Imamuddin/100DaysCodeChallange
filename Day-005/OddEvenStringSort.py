#using loops
s=input("Enter a string:")
s1=""
s2=""
for i in range(0,len(s),2): 
    s1+=s[i]
for i in range(1,len(s),2):     #Time Complexity:O(n)
    s2+=s[i]
print(s1+" "+s2)

print("-----------------------------------")
#using format string
s=input("Enter a string:")
print('{} {}'.format(s[::2], s[1::2]))    #Time Complexity:O(n)
print("-----------------------------------")
#using Slicing
s=input("Enter a string:")
print(s[::2] + ' ' + s[1::2])     #Time Complexity:O(n)
print("-----------------------------------")
#using format specifier
s=input("Enter a string:")
print('%s %s' % (s[::2], s[1::2]))    #Time Complexity:O(n)
print("-----------------------------------")

#using list
#->The enumerate() function is used to
#get both the index value of string i and the character from the string j.
s=input("Enter a string:")
odd, even = [], []
for i,j in enumerate(s):            #Time Complexity:O(n)
    even.append(j) if i % 2 == 0 else odd.append(j)
print("".join(even) + " " + "".join(odd))
