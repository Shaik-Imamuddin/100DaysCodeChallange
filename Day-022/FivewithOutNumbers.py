#5withoutnumbers!!

#Write a program that always prints 5
#Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/
#Good luck :)

#By using len of list
a = ['a','b','c','d','e']
print(len(a))       #Time Complexity:O(n)

#By using ord of this ""charecter
print(ord(""))     #Time Complexity:O(n)

#By using sum function along with range function
print(sum(range(len("learn"),len("python"))))       #Time Complexity:O(n)

#By using string index method
print('Support Ukraine!'.index('r'))        #Time Complexity:O(n)

#By using length of a string
print(len("five!"))     #Time Complexity:O(n)

#By using length of empty spaces it is same as above.
print(len("     "))     #Time Complexity:O(n)
