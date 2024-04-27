#FilterOutTheseGeese

#By using comparision Operator
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds=["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
for j in geese:    #For each element in geese
    for i in birds:    #For each element in birds 
        if i == j:
            birds.remove(i)                        #Time Complexity:O(n^2)
print(birds)

#By using in operator
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds=["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
for i in geese:
    if i in birds:          #Time Complexity:O(n^2)
        birds.remove(i)
print(birds)

#By using not in operator same as above program
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds=["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
l=[]
for i in birds:
    if i not in geese:          #Time Complexity:O(n^2)
        l.append(i)
print(l)

#By using list comprehension.
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds=["Mallard", "Barbary", "Hook Bill", "Pilgrim", "Blue Swedish", "Crested", "Toulouse"]
print([i for i in birds if i not in geese])     #Time Complexity:O(n^2)
