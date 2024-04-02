#Write a progarm to split a string and convert it into an array of words.

#convert string to list

#Using split() method
#The split() method iterates over each charecter of the string
s=input("Enter a sentence:")
l=s.split(" ")       #Time complexity:O(n)
print(l)


#using loop
s = input("Enter a sentence:")
arr = []
word = ""
for char in s:          #Time complexity:O(n)
    if char != " ":
        word += char
    else:
        arr.append(word)
        word = ""
arr.append(word)
print(arr)


#using list comprehension
s = input("Enter a sentence:")
arr = [word for word in s.split()]        #Time complexity:O(n)
print(arr)
