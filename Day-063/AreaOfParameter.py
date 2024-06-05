#AreaOfPerimeter

#By using conditional statements
l=int(input())
w=int(input())
if l==w:
    print(l*w)      #Time Complexity:O(1)
else:
    print((l+w)*2)

#we can compress the code 
l=int(input())
w=int(input())
print((l+w)*2 if l!=w else l*w)     #Time Complexity:O(1)

#By using list Indexing
l=int(input())
w=int(input())
print([l*w , 2*(l + w)][l != w])        #Time Complexity:O(1)
