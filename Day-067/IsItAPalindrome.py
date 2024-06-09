#IsItAPalindrome

#By using join() method
s=input()
s=s.upper()
reverse="".join(x for x in s[::-1])     #Time Complexity:O(n)
print(reverse==s)
print("-------------------------------")

#By using conditional statements along with upper() method
s=input()           #Time Complexity:O(n)
print(True if s.upper() == s[::-1].upper() else False)
print("-------------------------------")

#By using conditional statements along with lower() method
s=input()           #Time Complexity:O(n)
print(True if s.lower() == s[::-1].lower() else False)
