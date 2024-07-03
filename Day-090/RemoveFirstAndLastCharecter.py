#RemoveFirstAndLastCharecter

#By using string slicing along with len() method
s=input()
print(s[1:len(s)-1])        #Time Complexity:O(n)

#By using only string slicing
s=input()
print(s[1:-1])      #Time Complexity:O(n)

#By using pop and join methods
s=input()
s = list(s)
s.pop()
s.pop(0)
print(''.join(s))       #Time Complexity:O(n)
