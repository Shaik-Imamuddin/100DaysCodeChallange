#RemoveTheExclamationMarkAtTheEndOfString


#By using endswith() string method

s=input()
if s.endswith("!"):         #Time Complexity: O(n)
    s = s[:-1] 
print(s)

#We Can compress the above code to a single line
s=input()
print(s[:-1] if s.endswith("!") else s)     #Time Complexity: O(n)

#Only By using Conditional Statements

s=input()
if len(s)>1:
    if s[-1]=='!':          #Time Complexity: O(n)
        print(s[:-1])
    else:
        print(s)
