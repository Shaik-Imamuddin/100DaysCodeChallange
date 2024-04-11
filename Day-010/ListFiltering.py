#list filtering
#write a program that takes a list of non-negative integers and strings
#returns a new list with the strings filtered out.
#it has to return only integers

#The isinstance() function in Python is used to check if an object belongs to a specific class or type.
#It takes two parameters: the object whose type is to be checked, and the class or type itself.
#It returns True if the object is an instance of the specified class or type,otherwise it returns False.

#using list comprehension with isinstance() method
list=['a',45,'abc',56,'string','int',234]
print([i for i in list if isinstance(i, int)])      #Time complexity:O(n)
print("============================================")
list=['a',45,'abc',56,'string','int',234]
print([i for i in list if not isinstance(i, str)])      #Time complexity:O(n)
print("============================================")
#using list comprehension with type() method
list=[1,2,'aasf','1','123',123,'560','hi',520]
print([x for x in list if type(x) == int])          #Time complexity:O(n)
print("============================================")
#By using for loop
list=[1,2,'aasf','1','123',123]
l=[]
for i in list:
    if type(i)==int:            #Time complexity:O(n)
        l.append(i)
print(l)
