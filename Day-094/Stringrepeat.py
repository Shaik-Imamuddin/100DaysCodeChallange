#Stringrepeat

#By using String Concatination along with for loop
repeat=int(input())
string=input()
solution = ""
for i in range(repeat):     #Time Complexity:O(n)
    solution += string
print(solution)

#By using join method
repeat=int(input())         
string=input()              #Time Complexity:O(n)
print("".join([string]*repeat))

#By using string multiplication
repeat=int(input())
string=input()          #Time Complexity:O(n)
print(str(string) * repeat)

#By using list along with join method
repeat=int(input())
string=input()
hill = []                   #Time Complexity:O(n)
for k in range(repeat):
    hill.append(string)
print(''.join(hill))

#By using formatted strings
repeat=int(input())                 #Time Complexity:O(n)
string=input()
print(f"{string * repeat}")
