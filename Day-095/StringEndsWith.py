#StringEndsWith

#By using endswith method
string=input()
ending=input()
print(string.endswith(ending))      #Time Complexity:O(n)

#By using in operator along with string slicing
string=input()
ending=input()
print(ending in string[-len(ending):])  #Time Complexity:O(n)

#By using double equal to operator
string=input()
ending=input()
print(ending == string[0-len(ending):]) #Time Complexity:O(n)


#By using endswith method along with conditions
string=input()
ending=input()
if string.endswith(ending):     #Time Complexity:O(n)
    print(True)
else:
    print(False)

#By using double equal to operator along with conditions
string=input()
ending=input()
if ending == string[-len(ending):]:print(True)      #Time Complexity:O(n)
else:print(False)
