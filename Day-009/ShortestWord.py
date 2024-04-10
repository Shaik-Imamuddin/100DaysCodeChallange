
#DESCRIPTION:
#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.


#using split method()
s=input()
print(len(min(s.split(' '), key=len)))      #Time Complexity : O(n)

print("-------------------------------------")

#using list
s=input()
l=s.split()
list=[]
for i in l:                 #Time Complexity : O(n)
    list.append(len(i))
print(min(list))

print("-------------------------------------")

#using tuple comprehension
s=input()
r=min(len(x) for x in s.split())        #Time Complexity : O(n)
print(r)
