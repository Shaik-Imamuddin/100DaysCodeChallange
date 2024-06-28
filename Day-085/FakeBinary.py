#FakeBinary

#By using conditional statements along with string concatination
x=input()
s=''
for i in x:
    if int(i)<5: s+='0'     #Time Complexity:O(n)
    else: s+='1'
print(s)

#By using join method along with conditional statements
x=input()
print(''.join('0' if c < '5' else '1' for c in x))  #Time Complexity:O(n)

#By using join method along with in operator and conditional statements
x=input()
print("".join("0" if n in "01234" else "1" for n in x)) #Time Complexity:O(n)

#By using join method along with list comprehension
x=input()
print(''.join([str(int(i) // 5) for i in x]))       #Time Complexity:O(n)
