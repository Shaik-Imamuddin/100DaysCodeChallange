#You are going to be given a word. Your job is to return the middle character of the word.
#If the word's length is odd, return the middle character.
#If the word's length is even, return the middle 2 characters.

#By using conditons
s=input("Enter a string:")
mid = len(s)//2 
if len(s) % 2 == 0:
    print(s[mid-1:mid+1])       #Time Complexity : O(n)
else:
    print(s[mid])
print("-------------------------")

#By using looping
s=input("Enter a string:")
while len(s) > 2:           #Time Complexity : O(n)
        s = s[1:-1]     
print(s)
print("-------------------------")

#by using slicing
s=input("Enter a string:")
print(s[(len(s)-1)//2:len(s)//2+1])  #Time Complexity : O(n)
print("-------------------------")
