#RemoveStringSpaces


#By using join method along with tuple comprehension
x=input()
print(''.join(i for i in x if i !=' '))     #Time Complexity: O(n)

#By using join method along with split method
x=input()
print("".join(x.split()))       #Time Complexity: O(n)

#By using Replace Method
x=input()
print(x.replace(' ',''))        #Time Complexity: O(n)

#By using string concatination along with for loop
x=input()
s=''
for i in x:             #Time Complexity: O(n)
    if i!=' ':
        s+=i
print(s)
